import scapy.all as scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst

        if packet.haslayer(scapy.TCP):
            tcp_src = packet[scapy.TCP].sport
            tcp_dst = packet[scapy.TCP].dport

            print(f"IP Source: {ip_src}, IP Destination: {ip_dst}")
            print(f"TCP Source Port: {tcp_src}, TCP Destination Port: {tcp_dst}")
            print("-" * 45)

# Set the network interface to listen on
interface = "lo"  # Replace with the name of your interface (e.g., "eth0" on Linux)

# Start packet capture
scapy.sniff(iface=interface, store=False, prn=packet_callback)
