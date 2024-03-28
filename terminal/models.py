from message.models import Message as MessageModel
from message.schemas import mobileBeacon as mobileBeaconSchema
from message.schemas import record as recordSchema

class Terminal:
    def __init__(self, terminal_id):
        self.terminal_id = terminal_id
        self.memory = []  # Para armazenar dados a serem enviados ou recebidos
        self.state = "SLEEP"  # Estados incluem: SLEEP, LISTENING, SOLICIT_TRANSM, WAITING_FOR_REPLY
        self.partner_terminal = None  # ID do terminal parceiro
        self.data_to_send = []  # Dados que este terminal deseja enviar
        self.data_to_receive = []  # Dados que este terminal deseja receber

        # fazer lógica de memoria máxima

    def sleep(self):
        self.state = "SLEEP"
        self.partner_id = None

    def wake_up(self):
        self.state = "LISTENING"
        self.listen_for_beacon()

    def listen_for_beacon(self):
        self.state = "LISTENING"
        self.emit_beacon()
        # Lógica para escutar beacons. Se nenhum beacon for detectado, emitir um.
        pass

    def emit_beacon(self):
        if self.state == "LISTENING":
            self.state = "WAITING_FOR_REPLY"  # adicionar temporização
            location = self.get_location()
            msg = self.serialize(mobileBeaconSchema(message_type=1, id=self.terminal_id, latitude=location['latitude'], longitude=location['longitude'],
                                     record_time=10))
            self.memory.append(msg)
        else:
            # Não emite beacon se não estiver em LISTENING
            pass

    def serialize(self, data: mobileBeaconSchema | recordSchema):

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

        message_bytes = msg.build() # se printar, aparecerá em hexadecimal por conta do Python, mas a representação interna é em binário.

        return message_bytes

    def get_location(self):
        # Retorna uma localização fixa, mas pode ser modificado para dinâmico
        return {"latitude": 40.7128, "longitude": -74.0060}

    def save_data(self, data):
        self.memory.append(data)

    def send_data(self):
        if self.state in ["WAITING_FOR_REPLY", "SOLICIT_TRANSM"]:
            # Envio dos dados acumulados
            self.state = "TRANSMITTING"
            record = self.memory
            self.memory = []
            return record
        else:
            # Caso não esteja esperando por resposta ou solicitando transmissão, não envia dados
            pass

    def receive_beacon(self, beacon):
        self.partner_terminal = beacon.id  # ver qual vai ser o formato do beacon (pode ser dict, json)
        self.save_data(beacon)

    def request_data_transmission(self):
        # Método para solicitar a transmissão de dados para o parceiro
        if self.state == "SOLICIT_TRANSM" and self.partner_id is not None:
            self.state = "WAITING_FOR_AK"
            if len(self.memory) == 0:
                self.emit_beacon()
            # Seria enviada uma solicitação de transmissão para o parceiro identificado por partner_id

    def send_metadata(self):
        # Enviar metadados sobre os dados que deseja transmitir ou receber
        pass

    def receive_metadata(self, metadata):
        # Receber e processar metadados do parceiro

        pass

    def solicit_data_transmission(self):
        self.state = "SOLICIT_TRANSM"
        if len(self.memory) == 0:
            self.emit_beacon()
        # Solicitar ao parceiro a transmissão dos dados
        pass

    def accept_data_reception(self):
        # Aceitar a recepção de dados do parceiro
        pass

    def transmit_data(self):
        # Lógica para transmitir dados ao parceiro
        pass

    def end_communication(self):
        # Encerrar a comunicação e voltar ao estado inicial
        self.state = "SLEEP"
        self.partner_terminal = None
