# Packet Sniffer

A simple network packet analyzer that captures and displays network traffic. **Educational purposes only.**

## ⚠️ Legal and Ethical Warning

**This tool is for educational learning purposes only.** Unauthorized network monitoring is illegal in most jurisdictions. Only use this tool:
- On your own network with permission
- In authorized testing environments
- For learning about network protocols
- In controlled educational settings

## Features

- Captures network packets in real-time
- Displays source and destination IP addresses
- Identifies protocol type (TCP, UDP, ICMP)
- Shows payload preview (first 50 bytes)
- Easy to use and understand

## Requirements

```
Python 3.6+
Scapy library
Administrative/Root privileges
```

## Installation

```bash
pip install scapy
```

## Usage

```bash
# On Linux/macOS:
sudo python packet-sniffer.py

# On Windows (run as Administrator):
python packet-sniffer.py
```

Press **Ctrl+C** to stop sniffing.

## Output Example

```
Source: 192.168.1.100 -> Destination: 8.8.8.8
Protocol: TCP
Payload: b'GET / HTTP/1.1\r\nHost: google.com\r\nUser-Agent...'

Source: 192.168.1.100 -> Destination: 192.168.1.1
Protocol: UDP
```

## How It Works

The script uses the `scapy` library to:
1. Capture packets from the network interface
2. Extract IP layer information (source, destination)
3. Identify the transport protocol (TCP, UDP, ICMP)
4. Display the packet payload (if available)

## Key Components

- **IP Layer**: Extracts source and destination IP addresses
- **Protocol Detection**: Checks for TCP, UDP, or ICMP layers
- **Payload Display**: Shows raw packet data (first 50 bytes)

## Advanced Usage

### Sniff Only TCP Packets
```python
sniff(prn=process_packet, filter="tcp", store=False)
```

### Sniff Only UDP Packets
```python
sniff(prn=process_packet, filter="udp", store=False)
```

### Sniff on Specific Interface
```python
sniff(prn=process_packet, iface="eth0", store=False)
```

## Learning Concepts

This project demonstrates:
- Network packet structure
- Protocol layers (IP, TCP, UDP, ICMP)
- Network interface monitoring
- Packet parsing and analysis

## Troubleshooting

**"Permission denied" error**: You need administrator/root privileges
```bash
sudo python packet-sniffer.py  # Linux/macOS
```

**Requires elevation**: Run Command Prompt/PowerShell as Administrator (Windows)

## License

MIT License - For educational purposes only.
