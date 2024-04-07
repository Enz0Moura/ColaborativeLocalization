import uuid

from message.models import Message as MessageModel
from message.schemas import totemACK as totemACKSchema


class Totem:
    def __init__(self):
        self.connected_terminals = {}
        self.id = 4000
        self.data_storage = []

    def max_records(self):
        """
        Método para verificação de espaço livre no totem
        """
        free_space = 12 - len(self.data_storage)
        return free_space

    def receive_beacon(self, beacon):
        # Processa beacons recebidos dos terminais
        beacon = MessageModel.parse(beacon)
        terminal_id = beacon["id"]
        if terminal_id not in self.connected_terminals:
            self.connected_terminals[terminal_id] = "CONNECTED"
            print(f"Totem: Beacon recebido e conectado ao Terminal {terminal_id}.")
            ack = self.accept_data_reception(beacon)
            ack_parsed = MessageModel.parse(ack)
            if ack_parsed['max_records'] > 0:
                print(f"Connection acepted with max records: {ack_parsed['max_records']}")
            else:
                print(f"Connection refused with max records: {ack_parsed['hop_count']}")
            return ack
        else:
            pass

    def accept_data_reception(self, beacon):
        """
        Aceitar a recepção de dados do terminal
        """

        if len(self.data_storage) > 8 or beacon['hop_count'] <= 5:
            ack = self.max_records()
        else:
            ack = 0

        return self.acknowledge_beacon(beacon, ack)

    def acknowledge_beacon(self, beacon, ack):
        print(f"Totem: Enviando confirmação de recepção do beacon para Terminal {beacon['id']}.")
        return self.ack_message(
            totemACKSchema(message_type=2, id=self.id, group_flag=beacon['group_flag'], location_time=beacon['location_time'],
                           latitude=beacon['latitude'], longitude=beacon['longitude'], max_records=ack))

    def ack_message(self, data: totemACKSchema):
        """
        Método para envio de mensagem de ack. A representação interna da mensagem está em hexadecimal para facilitar leitura, mas o dado real é binário
        """

        msg = MessageModel(
            message_type=data.message_type,
            id=data.id,
            latitude=data.latitude,
            longitude=data.longitude,
            group_flag=data.group_flag,
            record_time=0,
            max_records=data.max_records,
            hop_count=0,
            channel=0,
            location_time=data.location_time,
            help_flag=0,
            battery=0
        )
        message_bytes = msg.build()

        return message_bytes

    def store_data(self, data):
        self.data_storage.append(data)
        print("Totem: Dados recebidos e armazenados.")

    def send_data_to_terminal(self, terminal_id, data):
        print(f"Totem: Enviando dados para Terminal {terminal_id}.")

    def manage_connections(self):
        for terminal_id, state in self.connected_terminals.items():
            if state == "INACTIVE":
                self.disconnect_terminal(terminal_id)

    def disconnect_terminal(self, terminal_id):
        if terminal_id in self.connected_terminals:
            del self.connected_terminals[terminal_id]
            print(f"Totem: Terminal {terminal_id} desconectado.")

    def send_memory(self):
        """
        Placeholder para função relacionada a banco de dados
        """

        register = self.data_storage
        self.data_storage = []
        return register
