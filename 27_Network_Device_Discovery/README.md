# 📡 Project 27: Network Device Discovery (ARP Scanner)

**Focus:** Network Reconnaissance, Scapy, ARP Protocol, IPv4/MAC Mapping

---

## 📌 Overview
Ez a projekt egy hálózati felderítő eszköz (Scanner), amely az ARP (Address Resolution Protocol) segítségével feltérképezi a helyi hálózatot (LAN). Az eszköz "Broadcast" csomagokat küld szét, és listázza az összes aktív eszköz IP- és MAC-címét.

## ⚙️ Features
* **Active Scanning:** Nem a gyorsítótárat olvassa, hanem valós időben kérdezi le az eszközöket.
* **Broadcast Mechanism:** A `ff:ff:ff:ff:ff:ff` címzés használata a teljes hálózat eléréséhez.
* **Clean Output:** Átlátható táblázatba rendezi a talált klienseket.
* **Argparse Integration:** Parancssori argumentumokkal dinamikusan megadható a célzott IP-tartomány.

## 🛠️ Usage
A szkript futtatásához add meg a célzott hálózati tartományt CIDR formátumban (pl. `/24`):

```bash
python network_scanner.py -t 192.168.0.1/24