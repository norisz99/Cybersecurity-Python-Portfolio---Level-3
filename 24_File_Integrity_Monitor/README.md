# 🛡️ Project 24: File Integrity Monitor (FIM)

**Focus:** Defensive Security (Blue Team), Cryptography, System Auditing

---

## 📌 Overview
Ez a projekt egy professzionális fájlsértetlenség-ellenőrző eszköz, amely képes valós időben detektálni a fájlrendszeren végzett illetéktelen módosításokat. A szoftver kritikus védelmi vonalat képez a Ransomware támadások és a rendszerfájlok manipulálása ellen.

---

## ⚙️ Technikai Megvalósítás
Az eszköz a **SHA-256** segítségével hoz létre egyedi digitális ujjlenyomatokat minden figyelt fájlról.

### Főbb funkciók:
* **Baseline Generálás:** Alapállapot rögzítése a `baseline.txt` adatbázisba.
* **Aktív Monitorozás:** Folyamatos ellenőrzés (`MODIFIED`, `CREATED`, `DELETED` események).
* **Memóriahatékony Kezelés:** Blokkos fájlolvasás (4096 bájt), ami lehetővé teszi nagy méretű állományok vizsgálatát alacsony RAM használat mellett.

---

## ⚠️ Jogi Nyilatkozat (Disclaimer)
A repozitóriumban található kódok kizárólag oktatási és etikus kiberbiztonsági kutatási célokat szolgálnak. A szoftverek bármilyen engedély nélküli, rosszindulatú használata illegális és súlyos jogi következményeket vonhat maga után. [cite: 2026-02-04]