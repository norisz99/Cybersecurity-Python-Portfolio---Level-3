import scapy.all as scapy
import argparse

# Színek a profi megjelenéshez
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def get_arguments():
    parser = argparse.ArgumentParser(description="Hálózati Felderítő (ARP Scanner)")
    parser.add_argument("-t", "--target", dest="target", help="Cél IP tartomány (pl. 192.168.0.1/24)", required=True)
    return parser.parse_args()

def scan(ip):
    print(f"\n{CYAN}[*] Hálózat pásztázása: {ip}...{RESET}\n")
    
    # 1. ARP Kérés létrehozása (Kié ez az IP?)
    arp_request = scapy.ARP(pdst=ip)
    
    # 2. Ethernet keret létrehozása (Broadcast címzés: ff:ff:ff:ff:ff:ff)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # 3. A kettő összefűzése egy csomaggá
    arp_request_broadcast = broadcast/arp_request
    
    # 4. Csomag kiküldése és válaszok fogadása
    # timeout=1: 1 másodpercet vár a válaszra, utána továbbmegy
    # verbose=False: Ne szemetelje tele a képernyőt felesleges infóval
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Eredmények feldolgozása
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print(f"{GREEN}IP Cím\t\t\tMAC Cím{RESET}")
    print("-----------------------------------------")
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")

if __name__ == "__main__":
    options = get_arguments()
    scan_result = scan(options.target)
    print_result(scan_result)