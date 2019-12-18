from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver
from typing import List

class User:
    def __init__(self, nickname: str = None, auth: bool = False):
        self.__nickname = nickname
        self.__auth = auth

    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname) -> None:
        if not nickname:
            return
        
        self.__nickname = nickname

    @property
    def auth(self) -> bool:
        return self.__auth

    @auth.setter
    def auth(self, status: bool) -> None:
        self.__auth = status

    
class Message:
    def __init__(self, nickname: str, msg: str):
        self.__nickname = nickname
        self.__msg = msg

    @property
    def content(self) -> str:
        return f"{self.__nickname}: {self.__msg}"

class Server(ServerFactory):
    
    protocol = 'ServerProtocol'
    clients: List['ServerProtocol']
    messages: List[Message]

    def addNewClient(self, client):
        if client not in self.clients:
            self.clients.append(client)
    
    def removeClient(self, client):
        if client in self.clients:
            self.clients.remove(client)

    def login(self, nickname):
        for client in self.clients:
            if client.user.nickname == nickname:
                return False
        
        return True

    def sendToOthersUsers(self, clientFrom, msg:Message):
        if not clientFrom.user.auth:
            return
        
        # for client in self.clients:
        #     if client != clientFrom && client.user.auth:
        #         client.sendLine(msg.content.encode())

    def startFactory(self):
        self.clients = []
        print("Server started")

    def stopFactory(self):
        print("Server stoped")

