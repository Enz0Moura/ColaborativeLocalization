from terminal.models import Terminal as TerminalModel
from totem.models import Totem as TotemModel
from server.models import Server as ServerModel
from sim.strategies import send_terminal_beacons

bracelet = TerminalModel(terminal_id=1234)
totem = TotemModel()
server = ServerModel()
id = 1234

bracelet.listen_for_beacon(id)


send_terminal_beacons(bracelet.send_data(), totem)

server.receive_data(totem.send_memory())
print(bracelet.memory)
print(server.memory)
