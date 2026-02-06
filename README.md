
# 🛡️ Cybersecurity & Python Portfolio - Level 3

**Author:** [Paczok Norisz]  
**Focus:** Active Network Attacks, Man-in-the-Middle (MITM), Malware Simulation, Post-Exploitation

---

## 📌 Overview

Ez a repozitórium a kiberbiztonsági portfólió **harmadik, legfejlettebb szintje**. Míg az előző szintek az alapokra és a felderítésre fókuszáltak, itt a hangsúly az **aktív hálózati beavatkozásra (Active Interception)** és a **támadási láncok (Kill Chain)** szimulációjára helyeződik át.

A gyűjtemény 9 haladó Python eszközt tartalmaz, amelyek demonstrálják, hogyan képes egy támadó manipulálni a hálózati forgalmat, átvenni az irányítást távoli eszközök felett, és hogyan lehet ezek ellen védekezni.

---

## 📂 Project Catalog

### ⚔️ Network Attacks & Man-in-the-Middle (MITM)

| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[26_Network_Interceptor_Suite](./26_Network_Interceptor_Suite)** | Komplex keretrendszer, amely egyesíti a Packet Sniffing és ARP Spoofing technikákat a hálózati forgalom eltérítésére. | `scapy`, `ARP Poisoning`, Threading |
| **[27_Network_Device_Discovery](./27_Network_Device_Discovery)** | Aktív hálózati felderítő eszköz (ARP Scanner), amely valós időben térképezi fel a LAN-on lévő eszközöket és MAC címeket. | `scapy`, Network Mapping, ARP |
| **[28_DNS_Spoofing](./28_DNS_Spoofing)** | DNS-válaszok meghamisítása, amellyel a célszemély forgalma egy támadó szerverre irányítható át (pl. `bing.com` -> `attacker IP`). | `netfilterqueue`, UDP Spoofing, DNS Protocol |
| **[29_File_Interceptor](./29_File_Interceptor)** | Fejlett MITM eszköz, amely letöltés közben röptében cseréli ki a kért fájlokat (pl. `.exe`) egy rosszindulatú payloadra. | `netfilterqueue`, HTTP Manipulation, TCP Streams |

### 💀 Malware Simulation & Post-Exploitation

| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[23_Reverse_Shell](./23_Reverse_Shell)** | Teljes körű Backdoor implementáció, amely távoli parancssori hozzáférést biztosít a támadónak a szerver-kliens architektúrán keresztül. | `socket`, TCP Connection, Subprocess |
| **[21_Advanced_Keylogger](./21_Advanced_Keylogger)** | Háttérben futó billentyűzet-figyelő, amely rögzíti a leütéseket és képes azokat e-mailben vagy fájlban továbbítani. | `pynput`, Stealth, File I/O |
| **[22_Ransomware_Simulator](./22_Ransomware_Simulator)** | Oktatási célú zsarolóvírus-szimulátor, amely bemutatja a fájlrendszerrekurzív titkosítását és a kulcskezelést. | `cryptography`, Fernet (AES), Recursion |

### 🛡️ Defensive Mechanisms & Steganography

| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[24_File_Integrity_Monitor](./24_File_Integrity_Monitor)** | Védelmi eszköz, amely hash-alapú ellenőrzéssel (SHA-256) riaszt, ha kritikus rendszerfájlokat módosítanak. | `hashlib`, Integrity Check, Diffing |
| **[25_Steganography_Tool](./25_Steganography_Tool)** | Adatok elrejtése képekben (LSB technika), demonstrálva a titkos kommunikációs csatornák működését. | `Pillow (PIL)`, Bitwise Operations, Encoding |

---

## 🛠️ Technologies Used

* **Language:** Python 3.10+
* **Networking:** `scapy`, `socket`, `netfilterqueue`
* **Cryptography:** `cryptography`, `hashlib`
* **System:** `pynput`, `subprocess`, `os`
* **Environment:** Kali Linux (Network Attacks), Windows 10/11 (Clients), VS Code

---

## ⚠️ Jogi Nyilatkozat (Disclaimer)

A repozitóriumban található kódok kizárólag **oktatási és etikus kiberbiztonsági kutatási** célokat szolgálnak. A szoftverek bármilyen engedély nélküli, rosszindulatú használata illegális és súlyos jogi következményeket vonhat maga után. A készítő nem vállal felelősséget a kódok nem rendeltetésszerű használatáért. [cite: 2026-02-04]
