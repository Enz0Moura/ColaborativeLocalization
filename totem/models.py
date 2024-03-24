class Totem:
    def __init__(self):
        self.state = "INITIAL"
        self.received_data = []

    def initial_state(self):
        self.state = "INITIAL"

    def receive_data(self, data):
        # Handle reception of data from a bracelet
        self.received_data.append(data)

    def evaluate_data(self, data):
        # Placeholder for logic to evaluate which data to accept
        return True

    def send_acceptance(self):
        # Send acceptance message back to bracelet
        pass

    def send_beacon(self):
        # Emit a beacon with its own location and ID
        pass

    def send_data_received(self):
        return self.received_data
