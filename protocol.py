import numpy as np
import soundfile as sf

SAMPLE_RATE = 44100
DURATION = 0.2
FREQ_0 = 1000
FREQ_1 = 2000

def encode_bits(bits, filename):
    signal = []
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
    for bit in bits:
        freq = FREQ_1 if bit == '1' else FREQ_0
        tone = np.sin(2 * np.pi * freq * t)
        signal.extend(tone)
    signal = np.array(signal)
    sf.write(filename, signal, SAMPLE_RATE)

def decode_bits(filename, threshold=1500):
    signal, sr = sf.read(filename)
    samples_per_bit = int(SAMPLE_RATE * DURATION)
    bits = ""
    for i in range(0, len(signal), samples_per_bit):
        chunk = signal[i:i+samples_per_bit]
        fft = np.fft.fft(chunk)
        freqs = np.fft.fftfreq(len(fft), 1/sr)
        peak_freq = abs(freqs[np.argmax(np.abs(fft))])
        bits += '1' if peak_freq > threshold else '0'
    return bits