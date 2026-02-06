import os
import hashlib
import time

# --- KONFIGURÁCIÓ ---
TARGET_PATH = "./files_to_watch"  # A figyelt mappa útvonala
BASELINE_FILE = "baseline.txt"    # Az adatbázis fájl helye
CHECK_INTERVAL = 1                # Ellenőrzési időköz (másodperc)

def calculate_sha256(file_path):
    """Kiszámítja a megadott fájl SHA-256 hash értékét."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None

def create_baseline():
    """Létrehozza a kiindulási állapotot a figyelt mappáról."""
    print(f"[*] Baseline generálása a következő mappához: {TARGET_PATH}...")
    baseline = {}
    
    for root, dirs, files in os.walk(TARGET_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_sha256(file_path)
            if file_hash:
                baseline[file_path] = file_hash

    # Mentés fájlba
    with open(BASELINE_FILE, "w") as f:
        for path, f_hash in baseline.items():
            f.write(f"{path}|{f_hash}\n")
    
    print(f"[+] Baseline sikeresen mentve: {BASELINE_FILE}")
    print(f"[*] Összesen {len(baseline)} fájl regisztrálva.\n")

def monitor():
    """Folyamatosan figyeli a változásokat a baseline alapján."""
    # Baseline betöltése a memóriába
    baseline = {}
    if not os.path.exists(BASELINE_FILE):
        print("[-] HIBA: Nincs baseline fájl! Először generáld le (Válaszd az 'A' opciót).")
        return

    with open(BASELINE_FILE, "r") as f:
        for line in f:
            path, f_hash = line.strip().split("|")
            baseline[path] = f_hash

    print(f"--- 🛡️ MONITOROZÁS INDÍTÁSA ({TARGET_PATH}) ---")
    
    while True:
        current_files = []
        for root, dirs, files in os.walk(TARGET_PATH):
            for file in files:
                file_path = os.path.join(root, file)
                current_files.append(file_path)
                
                # 1. Módosítás ellenőrzése
                current_hash = calculate_sha256(file_path)
                if file_path in baseline:
                    if current_hash != baseline[file_path]:
                        print(f"[⚠️ MODIFIED] {file_path}")
                        baseline[file_path] = current_hash # Frissítjük, hogy ne riasszon többször
                else:
                    # 2. Új fájl detektálása
                    print(f"[🆕 CREATED]  {file_path}")
                    baseline[file_path] = current_hash

        # 3. Törlés ellenőrzése
        deleted_files = []
        for path in baseline:
            if path not in current_files:
                print(f"[🚨 DELETED]  {path}")
                deleted_files.append(path)
        
        for path in deleted_files:
            del baseline[path]

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("--- 🔬 FILE INTEGRITY MONITOR (FIM) ---")
    print("A) Baseline létrehozása (Alapállapot rögzítése)")
    print("B) Monitorozás indítása (Változások figyelése)")
    choice = input("\nVálasz: ").upper()

    if choice == "A":
        create_baseline()
    elif choice == "B":
        monitor()
    else:
        print("Érvénytelen választás.")