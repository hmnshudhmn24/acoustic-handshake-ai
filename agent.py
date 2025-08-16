from protocol import encode_bits, decode_bits

class AcousticAgent:
    def __init__(self, name, handshake_code="1010"):
        self.name = name
        self.handshake_code = handshake_code
        self.in_secret_mode = False

    def send(self, message, filename):
        if self.in_secret_mode:
            bits = ''.join(format(ord(c), '08b') for c in message)
            encode_bits(bits, filename)
        else:
            with open(filename, 'w') as f:
                f.write(message)

    def receive(self, filename):
        try:
            with open(filename, 'r') as f:
                message = f.read()
            if message == self.handshake_code:
                self.in_secret_mode = True
            return message
        except UnicodeDecodeError:
            bits = decode_bits(filename)
            chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
            return ''.join(chars)