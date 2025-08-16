# 🎶 Acoustic Handshake AI 🤝🔊

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red.svg)](#)  
[![Stars](https://img.shields.io/github/stars/yourusername/acoustic-handshake-ai?style=social)](https://github.com/yourusername/acoustic-handshake-ai/stargazers)  

---

## 📖 Overview  

**Acoustic Handshake AI** is a playful and experimental communication system inspired by the viral **Gibberlink** idea.  

👉 Two AI agents start by exchanging a **public handshake** in human-readable **text**.  
👉 Once both agents verify each other, they secretly switch to **hidden audio communication** using **FSK (Frequency Shift Keying)** modulation.  

🔐 This combines **steganography, AI-inspired protocol design, and audio encoding** into a unique project that stands out on GitHub.  

---

## ✨ Features  

- 🤝 **Handshake Protocol** — Agents confirm identity via plain text exchange.  
- 🎧 **Secret Audio Mode** — Switch to sound-based encoding once handshake succeeds.  
- 📡 **FSK Encoding** — Uses **1000Hz (0)** and **2000Hz (1)** to represent binary.  
- 🗝️ **Steganography-lite** — Hide secret messages inside `.wav` files.  
- 🧪 **Demo Included** — Alice and Bob showcase how it works step by step.  

---

## 🛠️ Installation  

```bash
# Clone this repo
git clone https://github.com/yourusername/acoustic-handshake-ai.git
cd acoustic-handshake-ai

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage  

Run the demo to watch Alice & Bob perform their handshake and then exchange a secret audio message:  

```bash
python demo.py
```

### 💻 Example Output  

```
Bob received: 1010 (secret mode: True)
Alice received: 1010 (secret mode: True)
Bob decoded secret: Hello Bob!
```

---

## 📂 Project Structure  

```
acoustic-handshake-ai/
│── protocol.py        # Audio encoding/decoding (FSK modulation)
│── agent.py           # AI agent logic (handshake + secret mode)
│── demo.py            # Example run with Alice and Bob
│── requirements.txt   # Dependencies (numpy, soundfile)
│── README.md          # Project documentation
```

---

## 🎨 Demo Illustration  

Here’s how the communication works:  

```
Alice: "1010"  (plain text)  --->  Bob
Bob:   "1010"  (plain text)  --->  Alice
✅ Both switch to secret audio mode
Alice: "Hello Bob!" (hidden in sound) ---> Bob
Bob:   Decodes the message 🎉
```

---

## 🚀 Roadmap  

- [ ] Add noise-resilient encoding  
- [ ] Add spectrogram visualization of audio  
- [ ] Extend to multi-agent communication  
- [ ] Integrate real-time microphone I/O  

---

## 🧑‍💻 Contributing  

Contributions are welcome! 🙌  

1. Fork this repo 🍴  
2. Create a new branch 🌱  
3. Commit your changes 📝  
4. Open a Pull Request 🚀  

---

## ⭐ Support  

If you find this project interesting, please **star ⭐ the repo** — it helps more people discover it and motivates me to build more cool AI projects!  

---

## 📜 License  

This project is licensed under the **MIT License** — feel free to use, modify, and share. 
