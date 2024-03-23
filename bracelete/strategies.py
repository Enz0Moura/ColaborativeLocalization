def pack_lat_long(latitude, longitude):
    lat_packed = int((latitude + 90) * (2**24 / 180))
    long_packed = int((longitude + 180) * (2**24 / 360))

    return (lat_packed, long_packed)

def unpack_lat_long(lat_packed, long_packed):
    latitude = (lat_packed * (180 / 2**24)) - 90
    longitude = (long_packed * (360 / 2**24)) - 180

    return (latitude, longitude)


