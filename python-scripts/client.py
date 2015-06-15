import socket
from datetime import datetime, time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a client socket
port=9999

# get the current date-time
time1=datetime.now()

s.connect(("10.0.0.2", port)) # connect to server socket which is at address 10.0.0.2 and port 9999
tm=s.recv(1024) # this will read atmost 1024 bytes

# get the current date-time (after receiving current time from server)
time2=datetime.now()

serverTime=datetime.strptime(tm, "%Y-%m-%d %H:%M:%S.%f")

# terminate client socket
s.close()

# printing out time received from the time-server in console
print("The time got from the server is: \n")
print "Hour: %d \n" % serverTime.hour
print "Minute: %d \n" % serverTime.minute
print "Second: %d \n" % serverTime.second
print "Microsecond: %d \n" %serverTime.microsecond

# Applying Cristian`s algorithm
t1=time1.second*1000000+time1.microsecond
t2=time2.second*1000000+time2.microsecond
diff=(t2-t1)/2

# computed value of actual micro-sec time to be added to obtained server time
newMicro = serverTime.microsecond+diff

# printing out actual time in console after application of Cristian`s algorithm
print("Applying Cristian`s algorithm the actual time is: \n")
print "Hour: %d \n" % serverTime.hour
print "Minute: %d \n" % serverTime.minute
print "Second: %d \n" % serverTime.second
print "Microsecond: %d \n" % newMicro
