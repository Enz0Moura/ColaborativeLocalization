from terminal.models import Terminal as TerminalModel
from totem.models import Totem as TotemModel
from server.models import Server as ServerModel
from sim.strategies import interaction_bracelet_totem

bracelet1 = TerminalModel(terminal_id=1234)
bracelet2 = TerminalModel(terminal_id=4321)
totem = TotemModel()
server = ServerModel()
id = 1234

bracelet1.wake_up()

interaction_bracelet_totem(bracelet1, totem)

server.receive_data(totem.send_memory())

print(server.memory)
