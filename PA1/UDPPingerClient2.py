import socket #error with from socket import* Importing the libraries that I needed separately fixed the issue

from socket import AF_INET, SOCK_DGRAM

import time

print "Running" #Statement to let me know the program started correctly

serverName = '127.0.0.1' #server set as general computer ip

clientSocket = socket.socket(AF_INET,SOCK_DGRAM) #create the socket

clientSocket.settimeout(1) #sets the timeout at 1 second

sequence_number = 1 #variable to keep track of the sequence number

while sequence_number<=10:

    message = 'Ping' #message to be sent

    start=time.time() #assigns the current time to a variable

    clientSocket.sendto(message,(serverName, 12000))#sends a message to the server on port 12000

    try:

        message, address = clientSocket.recvfrom(1024) #recieves message from server

        elapsed = (time.time()-start) # calculates how much time has elapsed since the start time

        print sequence_number

        print message

        print 'Round Trip Time is:' + str(elapsed) + ' seconds' #issue with printing elapsed unless it was changed to a string

    except socket.timeout: #if the socket takes longer that 1 second, it does the following instead of the try

        print sequence_number

        print 'Request timed out'

    sequence_number+=1 #sequence number is increased after all of the other statements in the while

    if sequence_number > 10: #closes the socket after 10 packets

        clientSocket.close()