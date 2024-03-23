from construct import Struct, BitStruct, Flag, BitsInteger, Padding, bytes2str

message_schema = BitStruct(
    "message_type" / Flag,
    "id" / BitsInteger(15),
    "latitude" / BitsInteger(24),
    "longitude" / BitsInteger(24),
    "group_flag" / Flag,
    "record_time" / BitsInteger(16),
    "max_records" / BitsInteger(11),
    "hop_count" / BitsInteger(4),
    "channel" / BitsInteger(2),
    "location_time" / BitsInteger(16),
    "help_flag" / BitsInteger(2),
    "battery" / BitsInteger(4),
)

class Message:
    def __init__(self, **kwargs):
        self.data = kwargs

    def build(self):
        return message_schema.build(self.data)

    @staticmethod
    def parse(data):
        parsed_data = message_schema.parse(data)
        return Message(**parsed_data)


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



