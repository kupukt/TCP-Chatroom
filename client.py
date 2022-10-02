import socket
import threading

#Ip address and port
host = '10.50.109.109'
port = 2077

# Variable to find the name of the client
name = input("What is your name: ")

#Create the socket connection and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

#Receive a message
def receive():
    while True:
        try:

            #Message from server asking for name and if not, print message from another client.
            message = client.recv(1024).decode('utf-8')
            if message == 'Your Name: ':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error occured')
            client.close()
            break

def send_a_message():
    while True:
        message = f"{name}: {input('')}"
        client.send(message.encode('utf-8'))

receivethread = threading.Thread(target = receive)
receivethread.start()

sendthread = threading.Thread(target=send_a_message)
sendthread.start()
