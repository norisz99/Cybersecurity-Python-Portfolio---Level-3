# 🛡️ File Integrity Monitor (FIM)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-Hashlib-green?style=flat-square)
![Category](https://img.shields.io/badge/Category-Blue_Team-blue?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt egy professzionális fájlsértetlenség-ellenőrző eszköz, amely képes valós időben detektálni a fájlrendszeren végzett illetéktelen módosításokat. A szoftver kritikus védelmi vonalat képez a Ransomware támadások és a rendszerfájlok manipulálása ellen.

## 🛠️ Funkciók
* **📝 Baseline Generálás:** Alapállapot rögzítése a `baseline.txt` adatbázisba (SHA-256 hash).
* **👀 Aktív Monitorozás:** Folyamatos ellenőrzés (`MODIFIED`, `CREATED`, `DELETED` események).
* **⚡ Memóriahatékony Kezelés:** Blokkos fájlolvasás (4096 bájt), ami lehetővé teszi nagy méretű állományok vizsgálatát alacsony RAM használat mellett.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Algoritmus:** SHA-256 (Hashing)
* **Felhasználás:** Rendszerauditálás, védelem.

## 🚀 Használat
```bash
python fim.py
