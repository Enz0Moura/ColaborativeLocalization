from message.models import Message as MessageModel
from message.schemas import mobileBeacon as mobileBeaconSchema
from message.schemas import register as registerSchema
import threading



class Terminal:
    def __init__(self, terminal_id):
        self.terminal_id = terminal_id
        self.memory = []  # Para armazenar dados a serem enviados ou recebidos
        self.state = "SLEEP"  # Estados incluem: SLEEP, LISTENING, SOLICIT_TRANSM, WAITING_FOR_REPLY, TRANSMITTING
        self.partner_id = None  # ID do terminal parceiro
        self.ack_timer = None # Timer para reemitir beacon

    def sleep(self):
        self.state = "SLEEP"
        self.partner_id = None

    def wake_up(self, data=None):
        self.state = "ACTIVE"
        return self.listen_for_beacon(data)

    def listen_for_beacon(self, data=None):
        """
        Lógica para escutar beacons. Se nenhum beacon for detectado, emitir um.
        """
        self.state = "LISTENING"
        if data is None:
            return self.emit_beacon()

        else:
            self.state = "SOLICIT_TRANSM"
            self.receive_beacon(data)
            self.request_data_transmission()

    def emit_beacon(self):
        if self.state == "WAITING_FOR_ACK":
            self.state = "WAITING_FOR_REPLY"

            location = self.get_location()
            msg = self.serialize(mobileBeaconSchema(message_type=1, id=self.terminal_id, latitude=location['latitude'],
                                                    longitude=location['longitude'],
                                                    record_time=10))
            self.start_ack_timer(timeout=5.0)
            return self.send_data(msg)

        elif self.state == "TRANSMITTING":
            self.state = "WAITING_FOR_REPLY"  # adicionar temporização
            location = self.get_location()
            msg = self.serialize(registerSchema(message_type=1, id=self.terminal_id, latitude=location['latitude'],
                                                longitude=location['longitude'], group_flag=3,
                                                record_time=10, max_records=1, hop_count=10, channel=3, location_time=50,
                                                help_flag=0, battery=12))
            return self.send_data(msg)

        else:
            """
            Não emite beacon se não estiver em TRANSMITTING ou WAITINGFORACK
            """
            self.state = "ACTIVE"
            pass

    def serialize(self, data: mobileBeaconSchema | registerSchema):
        if isinstance(data, mobileBeaconSchema):
            msg = MessageModel(
                message_type=data.message_type,
                id=data.id,
                latitude=data.latitude,
                longitude=data.longitude,
                group_flag=0,
                record_time=data.record_time,
                max_records=0,
                hop_count=0,
                channel=0,
                location_time=0,
                help_flag=0,
                battery=0
            )
        elif isinstance(data, registerSchema):
            msg = MessageModel(
                message_type=data.message_type,
                id=data.id,
                latitude=data.latitude,
                longitude=data.longitude,
                group_flag=data.group_flag,
                record_time=data.record_time,
                max_records=data.max_records,
                hop_count=data.hop_count,
                channel=data.channel,
                location_time=data.location_time,
                help_flag=data.help_flag,
                battery=data.battery
            )

        message_bytes = msg.build()

        """
        Se printar message_bytes, a mensagem aparecerá em hexadecimal por conta da representação interna do print do Python, mas o dado está em binário.
        """

        return message_bytes

    def get_location(self):
        """
        Placeholder para método que retorna localização dinânmica do terminal.
        """
        return {"latitude": 40.7128, "longitude": -74.0060}

    def save_data(self, data):
        self.memory.append(data)
        return data

    def send_data(self, msg=None):
        """
        Método que retorna dados acumulados em um terminal ou um beacon emitido.
        """
        if self.state in ["WAITING_FOR_REPLY", "SOLICIT_TRANSM"]:
            self.state = "TRANSMITTING"
            if msg is not None:
                record = self.save_data(msg)
                return record
            record = self.memory
            self.memory = []
            return record
        else:
            """
            Caso não esteja esperando por resposta ou solicitando transmissão, não envia dados
            """
            pass

    def receive_beacon(self, beacon):
        beacon_parsed = MessageModel.parse(beacon)
        self.partner_id = beacon_parsed['id']
        print(f"Bracelet-{self.terminal_id} recieved Bracelet-{self.partner_id} beacon")
        self.save_data(beacon)

    def receive_ack(self, ack):
        ack_parsed = MessageModel.parse(ack)
        if ack_parsed is not None and ack_parsed['max_records'] > 0:
            print(f"Connection with totem-{ack_parsed['totem_id']} was accepted")
            self.ack_timer.cancel()
            return self.send_data()
        else:
            print(f"Connection with totem-{ack_parsed['totem_id']} was refused")
            return None

    def start_ack_timer(self, timeout=5.0):
        """
        Método para iniciar o temporizador de ACK
        """
        self.ack_timer = threading.Timer(timeout, self.handle_ack_timeout)
        self.ack_timer.start()

    def handle_ack_timeout(self):
        print("ACK não recebido a tempo.")
        self.state = "SLEEP"

    def request_data_transmission(self):
        """
        Método para solicitar a transmissão de dados para o parceiro
        """
        if self.state == "ACTIVE" and self.partner_id is None:
            self.state = "WAITING_FOR_ACK"
            if len(self.memory) == 0:
                self.state = "TRANSMITTING"
                return self.emit_beacon()
        else:
            self.state = "WAITING_FOR_REPLY"
            return self.send_data()

    def transmit_data(self):
        """
        Lógica para transmitir dados ao parceiro
        """
        pass



    def end_communication(self):
        """
        Método para encerrar a comunicação e voltar ao estado inicial
        """

        self.state = "SLEEP"
        self.partner_terminal = None
