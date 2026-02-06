from PIL import Image

def message_to_bin(message):
    """Szöveges üzenet átalakítása bináris sorozattá."""
    if isinstance(message, str):
        return ''.join([format(ord(i), "08b") for i in message])
    elif isinstance(message, bytes) or isinstance(message, bytearray):
        return ''.join([format(i, "08b") for i in message])
    elif isinstance(message, int):
        return format(message, "08b")

def encode_image(img_path, message, output_path):
    """Üzenet elrejtése a kép pixeljeiben."""
    img = Image.open(img_path).convert('RGB')
    binary_msg = message_to_bin(message) + '1111111111111110' # Delimiter a végére
    
    data_index = 0
    pixels = img.load()
    
    width, height = img.size
    for y in range(height):
        for x in range(width):
            # Pixel lekérése (R, G, B)
            r, g, b = pixels[x, y]
            
            # Red csatorna módosítása
            if data_index < len(binary_msg):
                r = (r & ~1) | int(binary_msg[data_index])
                data_index += 1
            # Green csatorna módosítása
            if data_index < len(binary_msg):
                g = (g & ~1) | int(binary_msg[data_index])
                data_index += 1
            # Blue csatorna módosítása
            if data_index < len(binary_msg):
                b = (b & ~1) | int(binary_msg[data_index])
                data_index += 1
            
            pixels[x, y] = (r, g, b)
            
            if data_index >= len(binary_msg):
                img.save(output_path)
                print(f"[+] Üzenet elrejtve ide: {output_path}")
                return

def decode_image(img_path):
    """Elrejtett üzenet kinyerése a képből."""
    img = Image.open(img_path).convert('RGB')
    pixels = img.load()
    binary_data = ""
    
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
            
    # Bináris adatok 8 bites darabokra bontása
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    
    # Karakterekké alakítás a delimiterig
    decoded_msg = ""
    for byte in all_bytes:
        if byte == "11111111": # Delimiter eleje
            break
        decoded_msg += chr(int(byte, 2))
        
    return decoded_msg

# --- FŐ PROGRAM ---
if __name__ == "__main__":
    print("--- 🎨 STEGANOGRAPHY TOOL ---")
    mode = input("E) Kódolás (Hide) | D) Dekódolás (Extract): ").upper()
    
    if mode == "E":
        msg = input("Titkos üzenet: ")
        encode_image("original.png", msg, "hidden.png")
    elif mode == "D":
        print(f"[*] Kinyert üzenet: {decode_image('hidden.png')}")