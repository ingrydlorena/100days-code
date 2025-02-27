'''
Day 88: Chat application
Implement a chat application using sockets.
'''

import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('urf-8')
            print(message)
        except:
            print("Disconnected from the server")
            client.close()
            break
def send_messages():
    while True:
        message = input()
        if message:
            client.send(message.enconde('utf-8'))

threading.Thread(target=receive_messages, daemon=True).start()
threading.Thread(target=send_messages, daemon=True).start()

while True:
    pass