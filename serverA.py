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

    while running:
        guess = clientsocket.recv(1024)
        guessstring = guess.decode('ascii')
        print(guessstring)
        
        guess = int(guessstring.split()[1])
        
        numberofguesses += 1
        running = 1
        
        if (guess == numbertoguess):
            messagetosend = ("Right Number!!!!\r\n")
            clientsocket.send(messagetosend.encode('ascii'))
            running = 0
                        
        else:
            # difference = abs(guess - numbertoguess)
            if guess < 3:
                messagetosend = ("It is Cold\r\n")
            else:
                messagetosend = ("It is Warm\r\n")
            
            clientsocket.send(messagetosend.encode('ascii'))
    
    clientsocket.close()
    print("Connection closed.")

def generatenumber():
    return random.randint(1, 5)


 



while 1:
    (clientsocket, clientaddress) = serversocket.accept()
    print("Connection received from: ", clientaddress)
    threading.Thread(target = focusclient, args =  (clientsocket, clientaddress)).start()
    print("Connection passed to new thread. Returning to listening.")
