from scapy.all import *

# Define the target IP address
target_ip = "192.168.0.253"

# Define a list to store sequence numbers
sequence_numbers = []

# Define a function to process TCP packets
def process_packet(packet):
    if IP in packet and TCP in packet:
        if packet[IP].src == target_ip:
            sequence_numbers.append(packet[TCP].seq)

# Load the pcap file
packets = rdpcap("extraction.pcapng")  # Replace with the actual file name

# Process each packet
for packet in packets:
    process_packet(packet)

# Combine sequence numbers and convert to bytes
sequence_bytes = b''.join(int(seq).to_bytes(4, byteorder='big') for seq in sequence_numbers)

# Decode to UTF-8 and print
decoded_text = sequence_bytes.decode('utf-8')
print(decoded_text)
