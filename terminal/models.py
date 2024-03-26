from message.models import Message as MessageModel


class Terminal:
    def __init__(self, terminal_id):
        self.terminal_id = terminal_id
        self.memory = []  # Para armazenar dados a serem enviados ou recebidos
        self.state = "SLEEP"  # Estados incluem: SLEEP, LISTENING, SOLICIT_TRANSM, WAITING_FOR_REPLY, etc.
        self.partner_terminal = None  # ID do terminal parceiro
        self.data_to_send = []  # Dados que este terminal deseja enviar
        self.data_to_receive = []  # Dados que este terminal deseja receber

    def sleep(self):
        self.state = "SLEEP"
        self.partner_id = None

    def wake_up(self):
        self.state = "LISTENING"
        self.listen_for_beacon()

    def listen_for_beacon(self):
        # Lógica para escutar beacons. Se nenhum beacon for detectado, emitir um.
        pass
    def emit_beacon(self):
        if self.state in ["LISTENING", "SLEEP"]:
            self.state = "WAITING_FOR_REPLY"
            location = self.get_location()
            msg = MessageModel(
                message_type=True,
                id=self.get_id(),
                latitude=location['latitude'],
                longitude=location['longitude'],
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
            self.memory.append(message_bytes)
            self.state = "WAITING_FOR_REPLY"
            return message_bytes
        else:
            # Não emite beacon se não estiver em SLEEP
            pass


    def get_location(self):
        # Retorna uma localização fixa, mas pode ser modificado para dinâmico
        return {"latitude": 40.7128, "longitude": -74.0060}

    def get_id(self):
        # Retorna o ID do Bracelete
        return 1234

    def save_data(self, data):
        self.memory.append(data)

    def send_data(self):
        if self.state in ["WAITING_FOR_REPLY", "SOLICIT_TRANSM"]:
            if len(self.memory) == 0:
                self.emit_beacon()
            else:
                # Envio dos dados acumulados
                self.state = "TRANSMITTING"
                beacons = self.memory
                self.memory = []
                return beacons
        else:
            # Caso não esteja esperando por resposta ou solicitando transmissão, não envia dados
            pass

    def receive_beacon(self, beacon, sender_id):
        self.partner_terminal = sender_id
        self.save_data(beacon)
        if self.state == "LISTENING":
            # Se estava no estado INICIAL e recebe um beacon, passa a solicitar transmissão
            self.state = "SOLICIT_TRANSM"
            self.partner_id = beacon.id

    def request_data_transmission(self):
        # Método para solicitar a transmissão de dados para o parceiro
        if self.state == "SOLICIT_TRANSM" and self.partner_id is not None:
            self.state = "WAITING_FOR_DATA"
            # Seria enviada uma solicitação de transmissão para o parceiro identificado por partner_id

    def send_metadata(self):
        # Enviar metadados sobre os dados que deseja transmitir ou receber
        pass

    def receive_metadata(self, metadata):
        # Receber e processar metadados do parceiro
        pass

    def solicit_data_transmission(self):
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
