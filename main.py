from bracelet.models import Bracelete as BraceletModel
from totem.models import Totem as TotemModel
from server.models import Server as ServerModel


bracelet = BraceletModel()
totem = TotemModel()

beacon = bracelet.send_data()

totem.receive_data(beacon)



