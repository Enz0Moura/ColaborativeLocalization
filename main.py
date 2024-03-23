from bracelete.models import message_schema
from bracelete.models import Message as MessageModel
import json
from construct import bytes2str


msg = MessageModel(
    message_type=True,
    id=12345,
    latitude=16777215,
    longitude = 16777215,
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


new_msg = MessageModel.parse(message_bytes)
print(new_msg.data)  