import random
from socket import *
import threading



serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(('localhost', 4000))
serversocket.listen(2)


def focusclient(clientsocket, clientaddress):

    clientgreeting = clientsocket.recv(1024)
    
    startmessage = "Guess on a number between 1 -5\r\n"
    clientsocket.send(startmessage.encode('ascii'))

    running = 1
    numberofguesses = 0
    
    numbertoguess = generatenumber()
