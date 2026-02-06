# 🦈 Project 26: Network Interceptor Suite

**Focus:** Network Security, ARP Spoofing, Packet Sniffing, Python Threading

---

## 📌 Overview
Ez a projekt egy integrált **Man-in-the-Middle (MitM)** keretrendszer, amely képes valós időben eltéríteni és elemezni a hálózati forgalmat egy helyi hálózaton belül. Az eszköz párhuzamos szálkezelést (threading) használ a hálózati mérgezés (ARP Spoofing) és az adatelemzés (Sniffing) egyidejű futtatásához.

---

## ⚙️ Features
* **Automated ARP Poisoning:** Folyamatosan hamisítja az ARP válaszokat a célpont és az átjáró között.
* **Real-time Traffic Analysis:** Figyeli és színezi a TCP/UDP/ICMP forgalmat.
* **Payload Inspection:** Megkísérli dekódolni a nyers adatcsomagokat (HTTP esetén olvasható szöveg, HTTPS esetén titkosított payload megjelenítése).
* **Auto-Restore Mechanism:** A program leállításakor automatikusan helyreállítja a hálózat eredeti állapotát.

---

## ⚠️ Technikai Tanulságok (Limitations)
A tesztek során bebizonyosodott, hogy a Python/Scapy alapú csomagkezelés nagy sávszélességű forgalom (pl. YouTube streaming) esetén szűk keresztmetszetet (bottleneck) okoz.
* **Jelenség:** A célpontnál az internetkapcsolat jelentősen belassul.
* **Ok:** A "User-space" csomagfeldolgozás lassúsága a Kernel-szintű routinghoz képest.
* **Konklúzió:** Éles környezetben, nagy adatforgalomhoz C++ vagy Go alapú eszközök (pl. Bettercap) javasoltak, de oktatási célra és protokoll-elemzésre ez a megoldás tökéletes.

---

## 🛠️ Usage
1.  **IP Forwarding engedélyezése (Windows):**
    `Set-NetIPInterface -Forwarding Enabled`
    *(Szükség esetén Registry módosítás: IPEnableRouter = 1)*
2.  **Futtatás:**
    ```bash
    python mitm_master.py -t [TARGET_IP] -g [GATEWAY_IP]
    ```

---

## ⚠️ Jogi Nyilatkozat (Disclaimer)
A repozitóriumban található kódok kizárólag oktatási és etikus kiberbiztonsági kutatási célokat szolgálnak. A szoftverek bármilyen engedély nélküli, rosszindulatú használata illegális és súlyos jogi következményeket vonhat maga után.