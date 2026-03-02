# 🎨 Steganography Tool (LSB Hiding)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-Pillow-green?style=flat-square)
![Category](https://img.shields.io/badge/Category-Cryptography-blue?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt a **Szteganográfia** működését mutatja be. A program a **Least Significant Bit (LSB)** eljárással rejt el szöveges üzeneteket PNG képekben, így a módosítás szabad szemmel láthatatlan marad.

## 📊 Vizuális vs. Bináris Eredmény
1. **👁️ Láthatatlanság:** Az `original.png` és a `hidden.png` vizuálisan teljesen azonos.
2. **🔓 Adatkinyerés:** A program képes a pixelek legkisebb helyiértékű bitjeiből hiba nélkül visszaállítani az elrejtett szöveget.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `PIL` (Pillow)
* **Módszer:** LSB (Least Significant Bit) manipuláció.

## 🚀 Használat
```bash
python stego.py
