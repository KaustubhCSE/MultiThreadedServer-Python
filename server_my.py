__author__ = 'KAUSTUBH MOHGAONKAR ID - 1001101770'

# Refrences :
# 1. http://ilab.cs.byu.edu/python/threadingmodule.html
# 2. http://stackoverflow.com/questions/20745352/creating-a-multithreaded-server-using-socketserver-framework-in-python
# 3. http://stackoverflow.com/questions/27218415/python-socket-programming-with-multiple-threads
# 4. http://stackoverflow.com/questions/5599872/python-windows-importerror-no-module-named-site
# 5. https://www.youtube.com/watch?v=wzrGwor2veQ

import socket,sys
import thread

def printdetails(connectionsocket): # Function to print the client details on server side.
    print "Client Details: "
    print "Socket Type: ", connectionsocket.type
    print "Socket Family: ", connectionsocket.family
    print "Socket Protocol: ", connectionsocket.proto
    print "Socket Timeout: ", connectionsocket._sock.gettimeout()
    print "Socket Peer Name: ", connectionsocket._sock.getpeername()

def socketoperation(connectionsocket, addr): # Function to initiate connection.

    try:
        result = connectionsocket.recv(1024)
        filename = result.split()[1].partition("/")[2]
        f = open(filename)
        print "\nClient Request Received!"
        printdetails(connectionsocket)
        connectionsocket.send("Response : HTTP/1.1 200 OK\n")
        connectionsocket.send("File Details: \n")
        connectionsocket.send(f.read())
        print "HTTP/1.1 200 OK"                                 # Response message for valid file.
        connectionsocket.close()
    except IOError:
        print "\nClient Request Received!"
        printdetails(connectionsocket)
        print "HTTP/1.1 404 Not Found"                          # Response message for file not found.
        connectionsocket.send("Response : HTTP/1.1 404 Not Found")
        connectionsocket.close()

try:
    server = sys.argv[1]    # command line example - python server_my.py servername port
    serverport = sys.argv[2]
except:
    print "Invalid or too less arguments entered at command line"
    server = "localhost"
    serverport = 12000
    print "Taking Default values : " + "Server: " + server + " Port: " + str(serverport)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Basic socket connection function in python.
serversocket.bind(('', int(serverport)))
serversocket.listen(1)

print "Server is Ready, Connected to Port: " + str(serverport)

while 1:
    connectionsocket, addr = serversocket.accept()
    thread.start_new_thread(socketoperation, (connectionsocket, addr,)) # inbuild function to initiate multithreaded operation.
    # socketoperation(connectionsocket, addr) -- use for single web server (without multithreading).