# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 🎭 Network File Interceptor

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-NetfilterQueue-red?style=flat-square)
![Category](https://img.shields.io/badge/Category-Malware_Injection-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt egy **File Interceptor** eszközt valósít meg, amely képes egy Man-in-the-Middle (MITM) támadás során a HTTP forgalom manipulálására. A script a `netfilterqueue` segítségével elfogja a célszemély hálózati csomagjait, és figyeli a letöltési kéréseket. Ha a célpont egy futtatható állományt (`.exe`) próbál letölteni, az eszköz röptében kicseréli azt egy előre megadott (rosszindulatú) fájlra.

## 🛠️ Funkciók
* **📦 Payload Injection:** Automatikusan felismeri a `.exe` letöltéseket és beilleszti a saját payload-ot.
* **🔧 Integrity Bypass:** Újraszámolja a TCP ellenőrzőösszegeket (Checksum) és a szekvenciaszámokat, hogy a kapcsolat ne szakadjon meg.
* **🐧 Linux Support:** NetfilterQueue alapú, így Linux környezetben (pl. Kali, Ubuntu) futtatható.

## 🚀 Használat
1. **Előfeltételek (Queue beállítása):**
   ```bash
   iptables -I FORWARD -j NFQUEUE --queue-num 0
