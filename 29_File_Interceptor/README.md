# 🎭 Project 29: Network File Interceptor

**Focus:** Network Manipulation, HTTP Protocol, Scapy, NetfilterQueue, MITM

---

## 📌 Overview
Ez a projekt egy **File Interceptor** eszközt valósít meg, amely képes egy Man-in-the-Middle (MITM) támadás során a HTTP forgalom manipulálására. A script a `netfilterqueue` segítségével elfogja a célszemély hálózati csomagjait, és figyeli a letöltési kéréseket. Ha a célpont egy futtatható állományt (`.exe`) próbál letölteni, az eszköz röptében kicseréli azt egy előre megadott (rosszindulatú) fájlra, miközben a felhasználó számára a letöltés folyamata zavartalannak tűnik.

## ⚙️ Features
* **Traffic Monitoring:** Valós időben elemzi az áthaladó HTTP forgalmat.
* **Payload Injection:** Automatikusan felismeri a `.exe` letöltéseket és beilleszti a saját payload-ot.
* **Integrity Bypass:** Újraszámolja a TCP ellenőrzőösszegeket (Checksum) és a szekvenciaszámokat, hogy a kapcsolat ne szakadjon meg.
* **Cross-Platform Support:** Python alapú, Linux környezetben (pl. Kali, Ubuntu) futtatható.

## 🛠 Usage
A script használata előtt biztosítani kell az IP Forwardingot és az `iptables` szabályokat (ahogy a Level 3 setupban megbeszéltük).

1. **Előfeltételek (Queue beállítása):**
   ```bash
   iptables -I FORWARD -j NFQUEUE --queue-num 0