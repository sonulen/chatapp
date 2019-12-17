from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver

class User:
    def __init__(self, nickname: str = None, auth: bool = False):
        self.__nickname = nickname
        self.__auth = auth

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname):
        if not nickname:
            return
        
        self.__nickname = nickname

    @property
    def auth(self):
        return self.__auth

    @auth.setter(self, status:bool):
        self.__auth = status
    

class Message:
    def __init__(self, nickname, msg):
        self.__nickname = nickname
        self.__msg = msg

    @property
    def content(self):
        return f"{self.__nickname}: {self.__msg}"



class Server(ServerFactory):
    
    protocol = ServerProtocol
    clients: list
    messages: list[Message]

    def addNewClient(self, client):
        if client not in self.clients:
            self.clients.append(client)
    
    def removeClient(self, client):
        if client in self.clients:
            self.clients.remove(client)

    def login(self, nickname)
        for client in clients:
            if client.user.nickname == nickname:
                return False
        
        return True

    def sendToOthersUsers(self, clientFrom, msg:Message):
        if not clienFromt.user.auth:
            return
        
        for client in clients:
            if client != clientFrom && client.auth:
                client.sendLine(msg.content.encode())

    def startFactory(self):
        self.clients = []
        print("Server started")

    def stopFactory(self):
        print("Server stoped")

