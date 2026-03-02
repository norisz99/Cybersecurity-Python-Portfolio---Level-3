# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 😈 DNS Spoofer

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-Scapy-orange?style=flat-square)
![Category](https://img.shields.io/badge/Category-Network_Manipulation-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt egy **DNS Spoofing** eszközt valósít meg, amely képes meghamisítani a tartománynév-feloldást (Domain Name Resolution) egy helyi hálózaton. A script figyeli a célpont DNS kéréseit (UDP 53), és hamis válaszokat küld vissza, átirányítva az áldozatot egy tetszőleges IP-címre (pl. egy támadó szerverre).

## 🛠️ Funkciók
* **👀 Traffic Monitoring:** Valós időben elemzi a DNS (UDP/53) forgalmat.
* **🎯 Target Recognition:** Szűri a kéréseket adott domainekre (pl. `www.bing.com`).
* **⚡ Forged Responses:** Szabványos DNS válaszcsomagokat generál és küld vissza a valódi szerver előtt ("Race Condition" kihasználása).
* **🌍 Cross-Platform:** Python és Scapy alapú, Linuxon és Windowson is futtatható.

## 🚀 Használat
A scriptet egy aktív Man-in-the-Middle támadás (pl. ARP Spoofing) közben kell futtatni.

1. **Konfiguráció:** Állítsd be a `TARGET_DOMAIN` és `REDIRECT_TO_IP` változókat a kódban.
2. **Futtatás:**
   ```bash
   python dns_spoofer.py
