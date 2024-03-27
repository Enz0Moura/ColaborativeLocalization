class Totem:
    def __init__(self):
        self.connected_terminals = {}
        self.data_storage = []
        # totem emite beacon! vários no tempo
    def receive_beacon(self, beacon, terminal_id):
        # Processa beacons recebidos dos terminais
        if terminal_id not in self.connected_terminals:
            self.connected_terminals[terminal_id] = "CONNECTED"
            self.acknowledge_beacon(terminal_id)
            print(f"Totem: Beacon recebido e conectado ao Terminal {terminal_id}.")
        else:
            pass

    def acknowledge_beacon(self, terminal_id):
        print(f"Totem: Enviando confirmação de recepção do beacon para Terminal {terminal_id}.")

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
        # Placeholder para função relacionada a banco de dados
        register = self.data_storage
        self.data_storage = []
        return register
