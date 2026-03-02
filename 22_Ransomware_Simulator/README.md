# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 💀 Ransomware Simulator (Educational)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Cryptography-Fernet-red?style=flat-square)
![Category](https://img.shields.io/badge/Category-Malware_Analysis-orange?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt a zsarolóvírusok (Ransomware) működési mechanizmusát és a kriptográfiai elveket demonstrálja egy biztonságos, ellenőrzött környezetben. A szoftver szimulálja, hogyan veszi át az irányítást egy támadó az áldozat fájljai felett, és hogyan állíthatóak azok helyre a váltságdíj (itt: a kulcs) birtokában.

A rendszer két fő komponensből áll:
1.  **Malware (The Encryptor):** AES-alapú titkosítással olvashatatlanná teszi a célfájlokat.
2.  **Decryptor (The Savior):** A generált szimmetrikus kulcs segítségével visszaállítja az eredeti állapotot.

## 🛠️ Funkciók
* **🔒 Fernet Encryption:** Szimmetrikus (AES-128 CBC módban működő) titkosítás a `cryptography` könyvtár segítségével.
* **🎯 "Sandbox" Működés:** A biztonság érdekében a program kizárólag a `test_files/` mappában lévő fájlokat támadja meg, a rendszer többi részét érintetlenül hagyja.
* **🔑 Key Management:** Automatikus titkosító kulcs generálás és mentés (`thekey.key`).
* **📄 File Discovery:** Rekurzív fájlkeresés a célkönyvtárban (szimulálva a valós kártevők terjedését).

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Algoritmus:** Fernet (Symmetric Encryption)
* **Függőség:** `cryptography`
* **Támadott kiterjesztések:** Minden fájl a célmappában.

## 🚀 Telepítés és Használat

**1. Előkészületek**
Telepítsd a szükséges kriptográfiai könyvtárat:
```bash
pip install cryptography
