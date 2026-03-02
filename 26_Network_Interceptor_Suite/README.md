# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 🦈 Network Interceptor Suite (MITM)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-Scapy-orange?style=flat-square)
![Category](https://img.shields.io/badge/Category-MITM_Attack-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt egy integrált **Man-in-the-Middle (MitM)** keretrendszer, amely képes valós időben eltéríteni és elemezni a hálózati forgalmat egy helyi hálózaton belül. Az eszköz párhuzamos szálkezelést (threading) használ a hálózati mérgezés (ARP Spoofing) és az adatelemzés (Sniffing) egyidejű futtatásához.

## 🛠️ Funkciók
* **☠️ Automated ARP Poisoning:** Folyamatosan hamisítja az ARP válaszokat a célpont és az átjáró között.
* **📊 Real-time Traffic Analysis:** Figyeli és színezi a TCP/UDP/ICMP forgalmat.
* **🔓 Payload Inspection:** Megkísérli dekódolni a nyers adatcsomagokat (HTTP szöveg megjelenítése).
* **🔄 Auto-Restore Mechanism:** A program leállításakor automatikusan helyreállítja a hálózat eredeti állapotát.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `scapy`, `threading`
* **Korlátok:** Nagy sávszélességű forgalom (pl. YouTube) esetén lassulást okozhat a User-space feldolgozás miatt.

## 🚀 Használat
1. **IP Forwarding engedélyezése (Windows PowerShell):**
   ```powershell
   Set-NetIPInterface -Forwarding Enabled
