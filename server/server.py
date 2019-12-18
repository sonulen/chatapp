from ServerFactory import Server
from twisted.internet import reactor

reactor.listenTCP(1234, Server())
reactor.run()
