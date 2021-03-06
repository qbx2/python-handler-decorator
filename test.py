from decohandler import BaseHandler, handles


class ServerHandler(BaseHandler):
    @handles(0x12)
    def handle_hello(self):
        return 'hello'

    @handles(0x12)
    def handle_hello2(self):
        return 'hello2'

    @handles(0x34)
    def handle_bye(self):
        return 'bye'


class Client:
    def __init__(self):
        super().__init__()

        self.server = ServerHandler()

    def request(self, opcode):
        return self.server.handle(opcode)

    def hello(self):
        print(self.request(0x12))

    def bye(self):
        print(self.request(0x34))


client = Client()
client.hello()
client.hello()
client.bye()
client.bye()
