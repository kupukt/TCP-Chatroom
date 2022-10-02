import socket
import threading
from datetime import datetime

#Create time variable           
now = datetime.now()

current_time = now.strftime("%H:%M")

#Set the host ip address and port number
host = '10.50.109.109'
port = 2077

#Making a socket using a TCP connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Makes the server.
s.bind((host, port))
s.listen()

#Makes a list for clients that join the server and a list for the names of the clients.
clients = []
names = []

#Function to send a message to all clients in the server
def universalmessage(message):
    for client in clients:
        client.send(message)

#Receive messages from other clients.
def handle(client):
    while True:
        message = client.recv(1024)
        universalmessage(message)
        

#Main function that is constantly running
def main():
    while True:

        #Server accepts client
        client, address = s.accept()
        print(f'{address} has connected.')

        #Asks client for their name and saves it in a list.
        client.send('Your Name: '.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)

        #Send to everyone that a client has joined the chat.
        #Saves the time that the client joined the server.
        universalmessage(f'{name} has joined the chat, have fun!'.encode('utf-8'))
        print(f'{name} has joined the chat at {current_time}')
        
        #Starts a thread to handle multiple clients
        thread = threading.Thread(target = handle, args = (client,))
        thread.start()

main()
