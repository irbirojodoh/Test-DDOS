import socket
import threading
from itertools import count


def ftp_tcp_handshake(server_address, server_port):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the FTP server
        client_socket.connect((server_address, server_port))

        # Receive and print the welcome message from the server
        welcome_message = client_socket.recv(1024)
        print("Server response:", welcome_message.decode())

        # Close the connection
        client_socket.close()

    except Exception as e:
        print("Error:", str(e))

# Replace these values with your FTP server's address and port
ftp_server_address = "192.168.2.101"
ftp_server_port = 21

# Call the function with your FTP server details


def main():
    # Create a new thread
    thread1 = threading.Thread(target=ftp_tcp_handshake(ftp_server_address, ftp_server_port))
    thread2 = threading.Thread(target=ftp_tcp_handshake(ftp_server_address, ftp_server_port))
    thread3 = threading.Thread(target=ftp_tcp_handshake(ftp_server_address, ftp_server_port))
    thread4 = threading.Thread(target=ftp_tcp_handshake(ftp_server_address, ftp_server_port))
    thread5 = threading.Thread(target=ftp_tcp_handshake(ftp_server_address, ftp_server_port))
    thread6 = threading.Thread(target=ftp_tcp_handshake(ftp_server_address, ftp_server_port))
    thread7 = threading.Thread(target=ftp_tcp_handshake(ftp_server_address, ftp_server_port))
    thread8 = threading.Thread(target=ftp_tcp_handshake(ftp_server_address, ftp_server_port))

    # Start the thread
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()


if __name__ == "__main__":
    for i in count(0):
        main()
