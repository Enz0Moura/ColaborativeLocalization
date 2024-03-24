from message.models import Message as MessageModel
class Bracelete:
    def __init__(self):
        self.memory = []
        self.emit_beacon()
        self.state = "SLEEP"

    def sleep(self):
        self.state = "SLEEP"

    def emit_beacon(self):
        location = self.get_location()
        msg = MessageModel(
            message_type=True,
            id=12345,
            latitude=location['latitude'],
            longitude=location['longitude'],
            group_flag=True,
            record_time=12345,
            max_records=200,
            hop_count=10,
            channel=3,
            location_time=54321,
            help_flag=0,
            battery=12
        )

        message_bytes = msg.build()
        self.memory.append(message_bytes)
        return message_bytes

    def get_location(self):
        return {"latitude": 40.7128, "longitude": -74.0060}

    def get_id(self):
        return 1234

    def save_data(self, data):
        self.memory.append(data)

    def send_data(self):
        if len(self.memory) == 0:
            self.emit_beacon()
        beacons = self.memory
        self.memory = []
        return beacons

    def receive_beacon(self, beacon):
        self.save_data(beacon)



