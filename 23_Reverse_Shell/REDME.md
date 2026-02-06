# 📡 Reverse Shell (Backdoor)

## 📌 Áttekintés
Ez a projekt egy klasszikus "Reverse Shell" implementációt tartalmaz. A hagyományos kapcsolatokkal ellentétben (ahol a kliens csatlakozik a szerverhez), itt az "áldozat" gépe (Backdoor) kezdeményezi a kapcsolatot a "támadó" (C2 Server) felé. Ez a technika lehetővé teszi a tűzfalak megkerülését, mivel a kifelé menő forgalmat ritkábban blokkolják.

## 🛠️ Funkciók
* **C2 Server:** A támadó gépén fut, fogadja a kapcsolatot és parancsokat küld.
* **Reverse Connection:** Az áldozat gépe csatlakozik haza a támadóhoz.
* **Remote Command Execution (RCE):** Távoli parancsfuttatás a `subprocess` könyvtárral.
* **Cross-Platform:** Működik Windows és Linux rendszereken is.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `socket`, `subprocess`, `os`
* **Protokoll:** TCP/IP Socket Stream

## 🚀 Használat
1. **Server (Támadó):** `python server.py` (Várakozó módba áll).
2. **Client (Áldozat):** `python backdoor.py` (Csatlakozik a szerver IP-jére).

## ⚠️ Jogi Nyilatkozat
Ez az eszköz oktatási célokat szolgál a hálózati kommunikáció és a C2 (Command & Control) infrastruktúrák megértéséhez. Engedély nélküli használata tilos.