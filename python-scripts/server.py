import socket
from datetime import datetime, time
from time import sleep

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
serversocket.bind(("10.0.0.2",port))
serversocket.listen(5)
while True:
        clientsocket,addr=serversocket.accept() //get the client address
        print("Got a connection from %s" % str(addr))
        
        //get current date and time 
        currentTime=datetime.now()
        
        //hang-up for 2 seconds.. done for processing delay
        sleep(2)
        
        //send the time value only in string format
        clientsocket.send(str(currentTime))
        
        //terminate client connection
        clientsocket.close()
