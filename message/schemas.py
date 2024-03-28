from pydantic import BaseModel

class Beacon(BaseModel):
    message_type: int
    id: int
    latitude: float
    longitude: float

class mobileBeacon(BaseModel):
    message_type: int
    id: int
    record_time: int
    latitude: float
    longitude: float

class record(BaseModel):
    message_type: int
    id: int
    record_time: int
    latitude: float
    longitude: float
    group_flag: int
    record_time: int
    max_records: int
    hop_count: int
    channel: int
    location_time: int
    help_flag: int
    battery: int
