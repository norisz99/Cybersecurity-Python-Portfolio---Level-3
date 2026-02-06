# 😈 Project 28: DNS Spoofer

**Focus:** Network Manipulation, DNS Protocol, Scapy, Man-in-the-Middle

---

## 📌 Overview
Ez a projekt egy **DNS Spoofing** eszközt valósít meg, amely képes meghamisítani a tartománynév-feloldást (Domain Name Resolution) egy helyi hálózaton. A script figyeli a célpont DNS kéréseit (UDP 53), és hamis válaszokat küld vissza, átirányítva az áldozatot egy tetszőleges IP-címre (pl. egy támadó szerverre).

## ⚙️ Features
* **Traffic Monitoring:** Valós időben elemzi a DNS (UDP/53) forgalmat.
* **Target Recognition:** Szűri a kéréseket adott domainekre (pl. `www.bing.com`).
* **Forged Responses:** Szabványos DNS válaszcsomagokat generál és küld vissza a valódi szerver előtt ("Race Condition" kihasználása).
* **Cross-Platform:** Python és Scapy alapú, így Linuxon és Windowson is futtatható.

## 🛠️ Usage
A scriptet egy aktív Man-in-the-Middle támadás (pl. ARP Spoofing) közben kell futtatni.

1.  **Konfiguráció:** Állítsd be a `TARGET_DOMAIN` és `REDIRECT_TO_IP` változókat a scriptben.
2.  **Futtatás:**
    ```bash
    python dns_spoofer.py
    ```

---

## ⚠️ Jogi Nyilatkozat (Disclaimer)
A repozitóriumban található kódok kizárólag oktatási és etikus kiberbiztonsági kutatási célokat szolgálnak. A DNS forgalom engedély nélküli manipulálása súlyos törvénysértés.