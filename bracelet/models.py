class Bracelete:
    def __init__(self):
        self.memory = []
        self.state = "SLEEP"

    def sleep(self):
        self.state = "SLEEP"

    def emit_beacon(self):
        return {'location': self.get_location(), 'id': self.get_id()}

    def get_location(self):
        return "approximate_location"

    def get_id(self):
        return "bracelet_id"

    def save_data(self, data):
        self.memory.append(data)

    def send_data(self):
        pass

    def receive_beacon(self, beacon):
        self.save_data(beacon)



