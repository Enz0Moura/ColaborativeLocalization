def send_terminal_beacons(memory, totem):
    """placeholder para função que utilize LoRa"""
    for beacon in memory:
        totem.store_data(beacon)


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
