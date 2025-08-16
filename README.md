# Acoustic AI Handshake (Gibberlink-style)

This project demonstrates a playful AI communication system inspired by the **Gibberlink** idea. Two agents first exchange a public handshake in human-readable text. Once they confirm mutual identity, they switch to communicating in a *hidden audio protocol*.

## Features
- **Handshake Phase**: Agents exchange a code ("1010") via text files.
- **Secret Mode**: Switch to encoding/decoding binary messages in sound (FSK modulation).
- **Demo Script**: Shows Alice and Bob identifying one another and then exchanging a hidden message.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the demo:
   ```bash
   python demo.py
   ```

## Example Output
```
Bob received: 1010 (secret mode: True)
Alice received: 1010 (secret mode: True)
Bob decoded secret: Hello Bob!
```

## Notes
- Uses **1000Hz for '0'** and **2000Hz for '1'** in audio encoding.
- Audio is saved in `.wav` files which can be played back or analyzed.
- This is a simplified educational prototype, not robust against noise.
