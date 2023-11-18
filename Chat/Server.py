import socket
import threading
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Client says: {message}")
            if message == '#quit':
                break
            # Send the message back to all other clients.
            broadcast_message(message, client_socket)
        except Exception as e:
            print(f"Error: {str(e)}")
            break
    print("Client disconnected.")
    client_socket.close()
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                # If error, close Connection
                client.close()
                clients.remove(client)
if __name__ == "__main__":
    server_ip = '0.0.0.0'  #Listening at every address.
    server_port = 8888  # Server port, you can change what you want.

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f"Server is listening on {server_ip}:{server_port}")
    clients = []
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        clients.append(client_socket)
        #Create a thread to handle client connections.
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
