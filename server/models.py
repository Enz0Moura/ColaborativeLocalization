from message.models import Message as MessageModel
def Server():
    def __init__(self):
        self.state = "INITIAL"
        self.received_data = []

    def receive_data(self, data):
        for message in data:
            self.received_data.append(MessageModel.parse(message))


