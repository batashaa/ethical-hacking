import scapy.all as scapy 

def scan(ip):
    arp = scapy.ARP(pdst=ip) 
    print(arp.summary())

scan('192.168.31.1/24')

