'''
Day 88: Chat application
Implement a chat application using sockets.
'''

import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket, client_address):
    print(f'New connection: {client_address}')

    broadcast(f"New user joined the chat from {client_address[0]}:{client_address[1]}\n".encode("utf-8"), client_socket)

    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
            else:
                break
        except:
            break


def accept_connections():
    print("Server is running, waiting for clients to connect...")
    while True:
        client_socket, client_adress = server.accept()
        clients.append(client_socket)

        threading.Thread(target=handle_client, args=(client_socket, client_adress)).start()
accept_connections()