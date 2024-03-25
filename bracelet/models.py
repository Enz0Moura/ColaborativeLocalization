from message.models import Message as MessageModel


class Bracelete:
    def __init__(self):
        self.memory = []
        self.state = "SLEEP"
        self.partner_id = None  # ID do parceiro de comunicação (outro Bracelete)

    def sleep(self):
        self.state = "SLEEP"
        self.partner_id = None

    def emit_beacon(self):
        if self.state == "SLEEP":
            self.state = "INITIAL"
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

    def receive_beacon(self, beacon):
        self.save_data(beacon)
        if self.state == "INITIAL":
            # Se estava no estado INICIAL e recebe um beacon, passa a solicitar transmissão
            self.state = "SOLICIT_TRANSM"
            self.partner_id = beacon.id

    def request_data_transmission(self):
        # Método para solicitar a transmissão de dados para o parceiro
        if self.state == "SOLICIT_TRANSM" and self.partner_id is not None:
            self.state = "WAITING_FOR_DATA"
            # Seria enviada uma solicitação de transmissão para o parceiro identificado por partner_id

    def handle_data_transmission_request(self, partner_id):
        # Método para tratar uma solicitação de transmissão de dados recebida
        if self.state == "WAITING_FOR_REPLY":
            self.partner_id = partner_id
            self.state = "ACCEPT_TRANSMISSION"
