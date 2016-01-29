__author__ = 'KAUSTUBH MOHGAONKAR ID - 1001101770'

# Refrences :
# 1. http://ilab.cs.byu.edu/python/threadingmodule.html
# 2. http://stackoverflow.com/questions/20745352/creating-a-multithreaded-server-using-socketserver-framework-in-python
# 3. http://stackoverflow.com/questions/27218415/python-socket-programming-with-multiple-threads
# 4. http://stackoverflow.com/questions/5599872/python-windows-importerror-no-module-named-site
# 5. https://www.youtube.com/watch?v=wzrGwor2veQ

import time, sys, socket

def printdetails(connectionsocket):             #Function to print the server details on client side.
    print "\nServer Details: "
    print "Socket Type: ", connectionsocket.type
    print "Socket Family: ", connectionsocket.family
    print "Socket Protocol: ", connectionsocket.proto
    print "Socket Timeout: ", connectionsocket._sock.gettimeout()
    print "Socket Peer Name: ", connectionsocket._sock.getpeername()

try:
    server = sys.argv[1]                    # command line example: python client.py localhost 12000 upload.txt
    port = int(sys.argv[2])
    filename = sys.argv[3]
except IndexError:
    print "Invalid or too less arguments entered at command line"
    server = "localhost"
    port = 12000
    filename = "upload.txt"
    print "Taking Default values : " + "Server: " + server + " Port: " + str(port)

try :
    print "File Name: ", filename                           # File for which details are sent by the server.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = socket.gethostbyname(server)

    request = "GET /" + filename + " HTTP/1.1\nHost: " + server + "\n\n"
    s.connect((server_ip, port))

    startTime = time.time()
    s.send(request.encode())

    result = s.recv(4096)
    endTime = time.time()
    # s.close()

    RTT = (endTime - startTime) * 1000                              # Calculate round trip time for request

    printdetails(s)
    print "RTT = %.3f" % RTT + " milli seconds"
    print "\n"
    print("Server response and File details below:")
    print "\n"

    while len(result) > 0:
        print(result)
        result = s.recv(1024)
    s.close()
except IOError:
    print("Server Connection Error: Please check if server is running")
    s.close()
