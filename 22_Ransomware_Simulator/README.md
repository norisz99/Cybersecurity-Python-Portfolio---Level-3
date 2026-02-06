# 🔐 Ransomware Simulator (Educational)

## 📌 Áttekintés
Ez a projekt a zsarolóvírusok (Ransomware) működési mechanizmusát demonstrálja ellenőrzött környezetben. A szoftver két komponensből áll: egy titkosító ágensből ("Malware"), amely AES-128 titkosítással zárolja a fájlokat, és egy visszafejtő eszközből ("Decryptor"), amely a megfelelő kulcs birtokában helyreállítja azokat.

## 🛠️ Funkciók
* **AES-128 Encryption:** Szimmetrikus titkosítás a `cryptography` könyvtár segítségével.
* **Targeted Attack:** Kizárólag a kijelölt `test_files` mappában dolgozik a biztonság érdekében.
* **Key Management:** Automatikus kulcsgenerálás és mentés helyi fájlba.
* **Decryption Logic:** A titkosított adatok visszaállítása bináris szinten.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `cryptography.fernet`
* **Módszer:** Symmetric Key Encryption (Fernet).

## ⚠️ Jogi Nyilatkozat (Disclaimer)
Ez az eszköz kizárólag **oktatási célra** készült, a kriptográfia és a malware-elemzés megértéséhez. A kód módosítása rosszindulatú célokra, vagy mások adatainak engedély nélküli titkosítása súlyos bűncselekmény.