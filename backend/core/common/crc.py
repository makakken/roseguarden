def crc16(data: bytearray, offset=0, length=0):
    if data is None:
        raise Exception("No data to process crc16")  #
    if offset < 0 or offset > len(data) - 1:
        raise Exception("Invalid offset for crc16")  #
    if offset + length > len(data):
        raise Exception("Invalid offset + length for crc16")
    if length <= 0:
        length = len(data) - offset

    crc = 0xFFFF
    for i in range(0, length):
        crc ^= data[offset + i] << 8
        for j in range(0, 8):
            if (crc & 0x8000) > 0:
                crc = (crc << 1) ^ 0x1021
            else:
                crc = crc << 1
    return crc & 0xFFFF
