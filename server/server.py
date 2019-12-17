import * from ServerFactory
import * from ServerLineProtocol
from twisted.internet import reactor


reactor.listenTCP(1234, Server())
reactor.run()