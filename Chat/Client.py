import socket
import threading

def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
        if message == "#quit":
            break

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Server says: {message}")
        except:
            break

if __name__ == "__main__":
    server_ip = '127.0.0.1'  # IP address of the Chat Server
    server_port = 8888  # Port of the Chat Server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"Connected to {server_ip}:{server_port}")

    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))

    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()

    client_socket.close()
