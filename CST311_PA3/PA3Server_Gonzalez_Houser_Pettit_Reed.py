from socket import *
from socket import socket
import threading

# threading needed to allow the server program to host multiple connections 
# simultaneously as opposed to sequentially
# Thread function
def thread_accept(index, message, lock, sockets):
    connectionSocket, addr = serverSocket.accept()  # accept a client connection
    sockets.append(connectionSocket)                # store client sockets
    sentence = connectionSocket.recv(1024).decode() # sentence = Client X: Alice or Client Y: Bob
    print('Received from client: ' + sentence)
    with lock:                                      # use a lock to prevent simultaneous writes to message
        message.append(sentence)                    # keep track of which sentence arrived first
# START SERVER SETUP
#Assign TCP port number
serverPort = 12000
# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET,SOCK_STREAM)
#Assign IP address and port number to socket
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
#END SERVER SETUP
while True:
    sockets = list()        # keep track of the sockets to send our final message to
    threads = list()        # keep track of threads
    message = list()        # keep track of which message arrived first
    lock = threading.Lock() # lock to keep multiple clients from writing simultaneously
    # Start two threads
    for index in range(2):
        x = threading.Thread(target=thread_accept, args=(index,message,lock,sockets))
        threads.append(x)
        x.start()
    # Join two threads
    for index, thread in enumerate(threads):
        thread.join()
    print('Sent acknowledgement to both X and Y')

    # return message to all clients of which sent message before which
    # opted to use the same list of messages stored for ease of expansion beyond 2
    for i in sockets:
        for j in range(0, len(message)-1):
            returnSentence = message[j] + " received before " + message[j+1]
            i.send(returnSentence.encode())
        i.close()
    print(returnSentence)