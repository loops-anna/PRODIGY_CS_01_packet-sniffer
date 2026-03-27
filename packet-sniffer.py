"""
Simple Network Packet Analyzer (Educational Use Only)

This program captures network packets and displays:
- Source IP
- Destination IP
- Protocol (TCP/UDP/ICMP)
- Payload (short preview)

Important:
- Run with admin/root privileges
- Use only on authorized networks
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = "Other"

        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        print(f"\nSource: {src_ip} -> Destination: {dst_ip}")
        print(f"Protocol: {protocol}")

        # Show payload (if exists)
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"Payload: {payload[:50]}")  # first 50 bytes

def start_sniffing():
    print("Sniffing started... Press Ctrl+C to stop.")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffing()
