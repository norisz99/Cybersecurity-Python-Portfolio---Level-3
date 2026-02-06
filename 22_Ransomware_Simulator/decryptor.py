import os
from cryptography.fernet import Fernet

# --- KONFIGURÁCIÓ ---
TARGET_DIR = "test_files"
KEY_FILE = "the_secret.key"

def load_key():
    """Betölti a kulcsot a fájlból."""
    try:
        return open(KEY_FILE, "rb").read()
    except FileNotFoundError:
        print("❌ HIBA: Nincs meg a kulcs! A fájlok elvesztek.")
        exit()

def decrypt_files(key):
    print(f"--- 🔓 DECRYPTOR INDÍTÁSA: {TARGET_DIR} ---")
    
    # Fájlok keresése (ugyanaz a logika)
    files = []
    for file in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, file)
        if os.path.isfile(file_path) and file != "ransomware.py":
            files.append(file_path)

    # Visszafejtés
    for file in files:
        try:
            with open(file, "rb") as the_file:
                contents = the_file.read()
            
            # ITT A VARÁZSLAT: .decrypt() az .encrypt() helyett
            contents_decrypted = Fernet(key).decrypt(contents)
            
            with open(file, "wb") as the_file:
                the_file.write(contents_decrypted)
                
            print(f"[+] Helyreállítva: {file}")
            
        except Exception as e:
            print(f"[!] Hiba a {file} fájlnál. Talán már nincs titkosítva? ({e})")

    print("\n✨ SIKER! A fájlok újra olvashatók. ✨")

if __name__ == "__main__":
    secret_key = load_key()
    decrypt_files(secret_key)