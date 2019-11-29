from socket import *

print ("Tonys Guessing Game \n\n")
print ("Connecting to server...\n")


clientsocket = socket(AF_INET, SOCK_STREAM)

try:
    clientsocket.connect(('localhost', 4000))
except ConnectionRefusedError:
    print ("The connection was refused.")
    exit(0)
print("connected!\n")

message = "Hi you doing\r\n"
clientsocket.send(message.encode('ascii'))

response = clientsocket.recv(1024)
print(response.decode('ascii'))
