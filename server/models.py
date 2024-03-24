from message.models import Message as MessageModel
class Server():
    def __init__(self):
        self.state = "INITIAL"
        self.memory = []

    def receive_data(self, data):
        for message in data:
            self.memory.append(MessageModel.parse(message))


