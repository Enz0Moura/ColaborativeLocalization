from pydantic import BaseModel

class totemBeacon(BaseModel):
    message_type: int
    id: int
    latitude: float
    longitude: float

class totemACK(BaseModel):
    message_type: int
    id: int
    group_flag: int
    location_time: int
    latitude: float
    longitude: float


class mobileBeacon(BaseModel):
    message_type: int
    id: int
    record_time: int
    latitude: float
    longitude: float
    max_records: int
    hop_count: int
    channel: int
class terminalMessage(BaseModel):
    message_type: int
    id: int
    record_time: int
    latitude: float
    longitude: float
    location_time: int
    hop_count: int

class register(BaseModel):
    message_type: int
    id: int
    group_flag: int
    battery: int

class helpNot(BaseModel):
    message_type: int
    help_flag: int
    id: int
    group_flag: int
    latitude: float
    longitude: float

class helpRequest(BaseModel):
    message_type: int
    help_flag: int
    id: int
    group_flag: int
    record_time: int
    latitude: float
    longitude: float
    location_time: int

class leaderElection(BaseModel):
    message_type: int
    id: int
    group_flag: int
    battery: int