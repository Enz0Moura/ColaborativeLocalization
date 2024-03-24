class Totem:
    def __init__(self):
        self.state = "INITIAL"
        self.memory = []

    def initial_state(self):
        self.state = "INITIAL"

    def receive_data(self, data):
        # Recebe beacons do bracelete
        self.memory.append(data)

    def evaluate_data(self, data):
        # Placeholder para lógica de aceite de dados
        return True

    def send_acceptance(self):
        # Manda mensagem de aceite para o bracelete
        pass

    def send_beacon(self):
        # Emite beacon da própria localização e ID
        pass

    def send_memory(self):
        # Placeholder para função relacionada a banco de dados
        return self.memory
