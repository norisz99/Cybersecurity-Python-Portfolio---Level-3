# 📡 Network Device Discovery (ARP Scanner)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-Scapy-green?style=flat-square)
![Category](https://img.shields.io/badge/Category-Reconnaissance-blue?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt egy hálózati felderítő eszköz (Scanner), amely az ARP (Address Resolution Protocol) segítségével feltérképezi a helyi hálózatot (LAN). Az eszköz "Broadcast" csomagokat küld szét, és listázza az összes aktív eszköz IP- és MAC-címét.

## 🛠️ Funkciók
* **⚡ Active Scanning:** Nem a gyorsítótárat olvassa, hanem valós időben kérdezi le az eszközöket.
* **📢 Broadcast Mechanism:** A `ff:ff:ff:ff:ff:ff` címzés használata a teljes hálózat eléréséhez.
* **📋 Clean Output:** Átlátható táblázatba rendezi a talált klienseket.
* **🔧 Argparse Integration:** Parancssori argumentumokkal dinamikusan megadható a célzott IP-tartomány.

## 🚀 Használat
A szkript futtatásához add meg a célzott hálózati tartományt CIDR formátumban (pl. `/24`):

```bash
python network_scanner.py -t 192.168.0.1/24
