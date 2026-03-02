# 🕵️‍♂️ Advanced Keylogger (Educational)

# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

## 📌 Áttekintés
Ez a projekt egy fejlett megfigyelő szoftver (Spyware) működését demonstrálja. A program képes a billentyűleütések rögzítésére ("Logging") és a képernyő tartalmának időszakos mentésére ("Screenshotting"). A rögzített adatokat emberi fogyasztásra alkalmas, mondat-szintű formátumban tárolja.

## 🛠️ Funkciók
* **⌨️ Keylogging:** Minden billentyűleütés rögzítése a háttérben.
* **🧠 Smart Formatting:** A nyers karakterek helyett olvasható mondatokat generál (kezeli a Backspace, Space, Enter gombokat).
* **📸 Screenshot:** Automatikus képernyőmentés megadott időközönként.
* **🧵 Threading:** Párhuzamos szálkezelés a billentyűzetfigyelés és a fotózás egyidejű futtatásához.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtárak:** `pynput` (Input Hook), `Pillow` (Képfeldolgozás), `threading`, `logging`.
* **Kimenet:** `smart_log.txt` (szöveg) és `/screenshots` mappa (képek).

## ⚠️ Jogi Nyilatkozat (Disclaimer)

Ez az eszköz kizárólag **oktatási és saját rendszeren végzett kutatási célokra** készült. Mások megfigyelése beleegyezésük nélkül súlyos bűncselekmény.
