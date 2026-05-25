# JarvisMessenger

[![JARVIS](https://img.shields.io/badge/JARVIS-Scientific_Assurance-blueviolet)](https://github.com/kluth/jarvis-messenger)
[![Decentralized](https://img.shields.io/badge/Architecture-Decentralized-blue)](https://github.com/kluth/jarvis-messenger)
[![Secure](https://img.shields.io/badge/Security-Omni--Cryptographic-green)](https://github.com/kluth/jarvis-messenger)

> **A JARVIS-native, substrate-driven messaging system written in JRV and Shell.**  
> Universal, secure, peer-to-peer communication substrate with autonomous routing.

## 📁 Structure

```
jarvis-messenger/
├── messenger.jrv        # Core messaging protocol & routing (JRV)
├── substrate.jrv        # Communication substrate layer (JRV)
├── jur-console.sh       # CLI console interface
├── start-gui.sh         # GUI launcher
└── GEMINI.md            # Development guidelines
```

## 🚀 Quick Start

```bash
# CLI mode
./jur-console.sh

# GUI mode
./start-gui.sh
```

## 🔧 Protocol

The messenger uses the JARVIS substrate for peer discovery, message routing, and cryptographic verification. Communication follows the **append-only delta model** — every message is cryptographically signed, timestamped, and appended to an immutable ledger.

## 📄 License

MIT