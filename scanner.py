import scapy.all as scapy 

def scan(ip):
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

    print("IP\t\t\tMacAddr")
    print("------------------------------------------")
    #Iterate over all the answered list of devices
    for element in answered:
        #Print IP and macaddress of the connected devices
        print(element[1].psrc+"\t\t"+element[1].hwsrc)
 
    
scan('192.168.31.1/24')

