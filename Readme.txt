This is a readme file for CSE 5344 Project 1. Please follow the instructions to run both the client and server python files.

Name: Kaustubh Mohgaonkar
ID: 1001101770

Project Details:
IDE : Pycharm 4.5.3
Packages : None external

Instructions to run Server from command line:
1. Open command prompt and navigate to the folder cnproject1
2. Type python server_my.py servername port where servername is your servername and port the port you want your server to run on.
For ex: python server_my.py localhost 12000
3. If the program is executed without or with invalid or insufficient command line parameters, default values of servername(localhost) and port(12000) will be taken.
4. After the port is running you will see a confirmation message: Server is Ready, Connected to Port

Instructions to run Client from command line:
1. Open command prompt and navigate to the folder cnproject1
2. Type python client.py servername serverport filename where servername is your servername and port the port your server is running on and filename is the file details you want to fetch from server.
For ex: python client.py localhost 12000 upload.txt
3. If the program is executed without or with invalid or insufficient command line parameters, default values of servername(localhost), port(12000), filename(upload.txt) will be taken.
4. After running client, the request will be sent to server and details will be displayed on both the terminals.
5. RTT for the request will also be displayed on the client side.

Refrences: 
1. http://ilab.cs.byu.edu/python/threadingmodule.html
2. http://stackoverflow.com/questions/20745352/creating-a-multithreaded-server-using-socketserver-framework-in-python
3. http://stackoverflow.com/questions/27218415/python-socket-programming-with-multiple-threads
4. http://stackoverflow.com/questions/5599872/python-windows-importerror-no-module-named-site
5. https://www.youtube.com/watch?v=wzrGwor2veQ