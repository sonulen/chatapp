from twisted.internet.protocol import connectionDone
from twisted.protocols.basic import LineOnlyReceiver
from ServerFactory import Server,Message,User


class ServerProtocol(LineOnlyReceiver):
    factory: 'Server'
    
    def __init__(self):
        super().__init__()
        self.user = User()

    def connectionMade(self):
        self.factory.addNewClient(self)

    def connectionLost(self, reason=connectionDone):
        self.factory.removeClient(self)

    def lineReceived(self, line: bytes):
        try:
            content = line.decode()
        except:
            print("Incorrect content")
            return

        # Смогли декодировать сообщение
        # Проверим залогинен ли пользователь
        if self.user.auth:
            # Да, уже залогинен, отправим всем остальным сообщение
            msg = Message(self.user.nickname, content)
            self.factory.sendToOthersUsers(self, msg)
        else:
            # Нет, а строка это логин?
            if content.startswith("nickname: "):
                nickname = content.replace("nickname: ", "")
                # Пробуем юзера с таким именем добавить
                if self.factory.login(nickname):
                    # Все окей - залогинились
                    self.user = User(nickname, True)
                else:
                    self.sendLine("Can't login with this nickname")
            else:
                self.sendLine("You need login with u nickname".encode())
