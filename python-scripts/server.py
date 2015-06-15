import socket
from datetime import datetime, time
from time import sleep

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
serversocket.bind(("10.0.0.2",port))
serversocket.listen(5)
while True:
        clientsocket,addr=serversocket.accept()
        print("Got a connection from %s" % str(addr))
        currentTime=datetime.now()
        sleep(2)
        clientsocket.send(str(currentTime))
        clientsocket.close()
