from terminal.models import Terminal as TerminalModel
from totem.models import Totem as TotemModel
from server.models import Server as ServerModel
from sim.strategies import send_terminal_beacons

bracelet1 = TerminalModel(terminal_id=1234)
bracelet2 = TerminalModel(terminal_id=4321)
totem = TotemModel()
server = ServerModel()
id = 1234

bracelet1.listen_for_beacon(bracelet2.wake_up())
bracelet1.listen_for_beacon()

send_terminal_beacons(bracelet1.request_data_transmission(), totem)

server.receive_data(totem.send_memory())

print(server.memory)
