from scapy.all import sniff, get_if_list, conf
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

def packet_callback(packet):
    if IP in packet:
        ip = packet[IP]
        proto = ip.proto
        src_ip = ip.src
        dst_ip = ip.dst

        if proto == 1 and ICMP in packet:
            pname = "ICMP"
            ports = ""
        elif proto == 6 and TCP in packet:
            t = packet[TCP]
            pname = "TCP"
            ports = f"{t.sport}->{t.dport}"
        elif proto == 17 and UDP in packet:
            u = packet[UDP]
            pname = "UDP"
            ports = f"{u.sport}->{u.dport}"
        else:
            pname = f"IP(proto={proto})"
            ports = ""

        print(f"[{datetime.now().strftime('%H:%M:%S')}] Protocol: {pname}")
        print(f"Source IP: {src_ip} {'' if not ports else 'Port(s): ' + ports}")
        print(f"Destination IP: {dst_ip}")
        print("-" * 50)

default_ifaces = get_if_list()
print("Available interfaces:", ", ".join(default_ifaces))
iface = input("Enter interface name to sniff on (press Enter to auto-select): ").strip() or None

try:
    sniff(iface=iface, prn=packet_callback, filter="ip", store=0)
except RuntimeError:
    print("Layer-2 sniffing unavailable; falling back to Layer-3 sniff mode.")
    conf.L3socket
    sniff(prn=packet_callback, filter="ip", store=0)
