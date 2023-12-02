import socket
import struct
import binascii
import codecs
from itertools import count
from multiprocessing import Process

def send_raw_tcp_frame(destination_ip, destination_port, data):
    # Create a raw socket
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

    # Set the IP header manually (you might need to adjust this based on your needs)
    ip_header = struct.pack('!BBHHHBBH4s4s', 0x45, 0, 20 + len(data), 0, 0, 6, 0, 0, socket.inet_aton('192.168.1.1'), socket.inet_aton(destination_ip))

    # Combine the IP header and the data
    packet = ip_header + data

    # Send the packet
    raw_socket.sendto(data, (destination_ip, destination_port))

def send_frames(destination_ip, destination_port, data):
    for _ in count(0):
        send_raw_tcp_frame(destination_ip, destination_port, data)

if __name__ == "__main__":
    # Example usage
    destination_ip = '192.168.2.101'
    destination_port = 21

    with open('data.txt', 'rb') as file:
        data = file.read()

    bindata = binascii.unhexlify(data)

    # Create 8 processes
    processes = []
    for _ in range(4):
        process = Process(target=send_frames, args=(destination_ip, destination_port, bindata))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
