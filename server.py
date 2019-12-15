from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver


class ServerProtocol(LineOnlyReceiver):
    factory: 'Server'
    isLogined: bool = False
    nickname: str = None

    def connectionMade(self):
        if self not in self.factory.clients:
            self.factory.clients.append(self)

    def connectionLost(self, reason=connectionDone):
        self.factory.clients.remove(self)
 
    def sendToOthers(self, msg):
        for user in self.factory.clients:
            if user is not self and user.isLogined:
                user.sendLine(msg)

    def lineReceived(self, line: bytes):
        try:
            content = line.decode()
        except:
            print("Incorrect content")
            return


        if self.isLogined:
            content = f"{self.nickname}: {content}"
            self.sendToOthers(content.encode())
        else:
            if content.startswith("nickname: "):
                self.registerUser(content.replace("nickname: ", ""))
            else:
                self.sendLine("Choose your nickname".encode())

    def registerUser(self, nickname):
        accepted: bool = True

        for client in self.factory.clients:
            if client.isLogined and (nickname == client.nickname):
                accepted = False
                break

        if accepted:
            self.isLogined = True
            self.nickname = nickname
            self.sendLine(f"Welcome {self.nickname}!".encode())
        else:
            self.sendLine(f"User with nickname: {nickname} already in chat!".encode())


class Server(ServerFactory):
    
    protocol = ServerProtocol
    clients: list
    # messages

    def startFactory(self):
        self.clients = []
        print("Server started")

    def stopFactory(self):
        print("Server stoped")


reactor.listenTCP(1234, Server())
reactor.run()