import struct

def load_ruben(filename):
    with open(filename, 'rb') as f:
        header = f.read(10)  # Example header size
        magic, width, height, bit_depth = struct.unpack('<5sII', header)
        if magic != b'RUBEN':
            raise ValueError("Not a valid .ruben file")
        pixels = f.read()  # Rest is pixel data
    return width, height, pixels
