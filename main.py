from bracelet.models import Bracelete as BraceletModel
from totem.models import Totem as TotemModel
from server.models import Server as ServerModel
from sim.strategies import send_bracelet_beacons

bracelet = BraceletModel()
totem = TotemModel()
server = ServerModel()


send_bracelet_beacons(bracelet.send_data(), totem)

server.receive_data(totem.send_memory())

print(server.memory)
