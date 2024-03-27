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