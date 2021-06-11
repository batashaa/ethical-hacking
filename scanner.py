import scapy.all as scapy 

def scan(ip):
    arp = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    request = broadcast/arp
    print(request.summary())
    arp.show()
    broadcast.show()
    request.show()

scan('192.168.31.1/24')

