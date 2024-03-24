from construct import Struct, BitStruct, Flag, BitsInteger, Padding, bytes2str

from bracelete.strategies import cord_to_24bit, cord_from_24bit

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
        print(f"Original latitude: {kwargs['latitude']}, longitude: {kwargs['longitude']}")
        if 'latitude' in kwargs:
            kwargs['latitude'] = cord_to_24bit(kwargs['latitude'], -90, 90)
        if 'longitude' in kwargs:
            kwargs['longitude'] = cord_to_24bit(kwargs['longitude'], -180, 180)
        print(f"Converted to 24 bit - latitude: {kwargs['latitude']}, longitude: {kwargs['longitude']}")
        self.data = kwargs

    def build(self):
        return message_schema.build(self.data)

    @staticmethod
    def parse(data):
        parsed_data = message_schema.parse(data)
        if 'latitude' in parsed_data:
            parsed_data['latitude'] = cord_from_24bit(parsed_data['latitude'], -90, 90)
        if 'longitude' in parsed_data:
            parsed_data['longitude'] = cord_from_24bit(parsed_data['longitude'], -180, 180)
        data = dict(parsed_data)
        data.pop('_io', None)
        return data


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



