import struct

def save_ruben(filename, width, height, pixels):
    header = b'RUBEN'  # Magic number
    header += struct.pack('<I', width)
    header += struct.pack('<I', height)
    header += struct.pack('<B', 24)  # 24 bits for RGB
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(pixels)  # Assuming raw RGB data
