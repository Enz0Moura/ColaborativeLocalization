def interaction_bracelet_totem(bracelet, totem):
    """placeholder para função que utilize LoRa"""
    registers = request_transmission(bracelet, totem)
    if registers:
        for register in registers:
            totem.store_data(register)

def request_transmission(bracelet, totem):
    """
    Função para simular envio de mensagem de ack e aceite ou rejeição da transmissão.
    """
    ack = bracelet.request_data_transmission()

    tot_ack = totem.receive_beacon(ack)

    message = bracelet.receive_ack(tot_ack)

    if message:
        return message
    else:
        return None



def simulate_interaction(bracelet, totem):
    """
    Função que simula interação totem-bracelet
    """
    beacon = bracelet.emit_beacon()  # Totem emits a beacon

    bracelet.receive_beacon(beacon)  # Bracelet receives beacon and stores data

    bracelet.send_data()  # Bracelet sends data to totem

    for data in bracelet.memory:  # Totem receives data and decides whether to accept it
        if totem.evaluate_data(data):
            totem.receive_data(data)
