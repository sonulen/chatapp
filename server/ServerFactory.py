from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver
from typing import List
from ServerLineProtocol import ServerProtocol
from common import User, Message
from collections import deque

class Server(ServerFactory):
    protocol = ServerProtocol
    clients: List[ServerProtocol]
    messages: deque(maxlen=20)

    def addNewClient(self, client) -> None:
        if client not in self.clients:
            self.clients.append(client)
    
    def removeClient(self, client) -> None:
        if client in self.clients:
            self.clients.remove(client)

    def login(self, nickname) -> bool:
        for client in self.clients:
            if client.user.nickname == nickname:
                return False
        
        return True

    def sendToOthersUsers(self, clientFrom, msg:Message):
        if clientFrom.user.auth:
            for client in self.clients:
                if client.user.auth and client is not clientFrom:
                    client.sendLine(msg.content.encode())
                    
            self.messages.append(msg)

    def sendMeLastMessages(self, client):
        for msg in list(self.messages):
            print(msg)

        
        

    def startFactory(self):
        self.clients = []
        print("Server started")

    def stopFactory(self):
        print("Server stoped")

