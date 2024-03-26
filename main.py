from bracelet.models import Terminal as TerminalModel
from totem.models import Totem as TotemModel
from server.models import Server as ServerModel
from sim.strategies import send_bracelet_beacons

bracelet = TerminalModel()
totem = TotemModel()
server = ServerModel()


send_bracelet_beacons(bracelet.send_data(), totem)

server.receive_data(totem.send_memory())
print(bracelet.memory)
print(server.memory)
