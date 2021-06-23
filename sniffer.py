import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        host = packet[http.HTTPRequest].Host
        path = packet[http.HTTPRequest].Path
        url = host+path
        print(url)

        if packet.haslayer(scapy.Raw):
            p = packet[scapy.Raw].load
            print(p)

sniff("wlp1s0")


