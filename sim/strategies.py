def send_bracelet_beacons(bracelet, totem):
    """placeholder para função que utilize LoRa"""
    for beacon in bracelet.memory:
        totem.receive_data(beacon)

def simulate_interaction(bracelet, totem):
    # Totem emits a beacon
    beacon = totem.send_beacon()

    # Bracelet receives beacon and stores data
    bracelet.receive_beacon(beacon)

    # Bracelet sends data to totem
    bracelet.send_data()

    # Totem receives data and decides whether to accept it
    for data in bracelet.memory:
        if totem.evaluate_data(data):
            totem.receive_data(data)
