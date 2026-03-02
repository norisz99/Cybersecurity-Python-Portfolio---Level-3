

# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 📡 Reverse Shell (Backdoor)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-socket-yellow?style=flat-square)
![Category](https://img.shields.io/badge/Category-C2_Infrastructure-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt egy klasszikus "Reverse Shell" implementációt tartalmaz. A hagyományos kapcsolatokkal ellentétben (ahol a kliens csatlakozik a szerverhez), itt az "áldozat" gépe (Backdoor) kezdeményezi a kapcsolatot a "támadó" (C2 Server) felé. Ez a technika lehetővé teszi a tűzfalak megkerülését, mivel a kifelé menő forgalmat ritkábban blokkolják.

## 🛠️ Funkciók
* **💀 C2 Server:** A támadó gépén fut, fogadja a kapcsolatot és parancsokat küld.
* **🔌 Reverse Connection:** Az áldozat gépe csatlakozik haza a támadóhoz.
* **💻 Remote Command Execution (RCE):** Távoli parancsfuttatás a `subprocess` könyvtárral.
* **🌍 Cross-Platform:** Működik Windows és Linux rendszereken is.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `socket`, `subprocess`, `os`
* **Protokoll:** TCP/IP Socket Stream

## 🚀 Használat
1. **Server (Támadó):** ```bash
   python server.py

