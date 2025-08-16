from agent import AcousticAgent

def main():
    alice = AcousticAgent("Alice")
    bob = AcousticAgent("Bob")

    # Initial human-readable handshake
    handshake_file = "handshake.txt"
    alice.send("1010", handshake_file)
    msg = bob.receive(handshake_file)
    print(f"Bob received: {msg} (secret mode: {bob.in_secret_mode})")

    # Bob replies handshake
    bob.send("1010", handshake_file)
    msg = alice.receive(handshake_file)
    print(f"Alice received: {msg} (secret mode: {alice.in_secret_mode})")

    # Now in secret mode, send hidden messages
    alice.send("Hello Bob!", "secret.wav")
    secret_msg = bob.receive("secret.wav")
    print(f"Bob decoded secret: {secret_msg}")

if __name__ == "__main__":
    main()