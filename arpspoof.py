import scapy.all as scapy 

#Create ARP response packet
packet = scapy.ARP(op=2,pdst="192.168.31.19", hwdst="b4:c4:fc:ac:df:e0", psrc="192.118.31.1")


