# Mininet-Implementation-of-Cristian-s-Algorithm
Clock synchronization is carried out using Cristian`s algorithm, coded as python script and which is implemented in Mininet which is used for network virtualization.

Initially we need to setup a virtaul environment in our host operating system. For this purpose we need to download Virtualbox from https://www.virtualbox.org/ wiki/Downloads. There we ﬁnd diﬀerent binary releases for diﬀerent platform. Since we are working on windows platform we need to download VirtualBox 4.3.28 the latest one for Windows hosts. Then we need to download mininet virtual image which we can get from https://github.com/mininet/openflow-tutorial/wiki/ Installing-Required-Software. There we select either 32bit or 64bit version. For our project we are using 32bit one which is Virtual Machine Image (OVF format, 32-bit, Mininet 2.2.0). The OVF format can be imported into VirtualBox, VMware or other popular virtualization program. We can also install mininet using native installation from the source which is also present in the github repository.
Once downloaded, we need to setup virtualbox in our machine. After the installation process, we now run virtualbox. There we need to setup a virtual machine. The procedure is as follows :
1. On the top left corner of the window click on New.
2. Fill up the credentials by giving a name to the virtual machine, select type as Linux and version as 32bit.
3. Now provide a memory size for the virtual machine. You can leave this to default 512 MB.
4. On the next window choose Use an existing virtual hard drive ﬁle and browse to the folder where you downloaded the mininet virtual image.
5. Click on Create to create the speciﬁed virtual machine.
We also need to perform a quick conﬁguration before running the virtual machine. For that we need to follow the following steps :
1. Select the virtual machine on the left-hand panel of the virtual-box window.
2. Click on Settings and navigate to Network option.
3. Now click on Adapter 2 tab and inside there check Enable Network Adapter.
4. Choose Attached to as Host-only Adapter.
5
This is necessary since we will be do a SSH from the host system (in our case Windows) to the virtual machine. After setting up the virtual machine run it. We will be prompted to virtual console where we need to enter the username and password inorder to access it. Enter username as ’mininet’ and password also as ’mininet’. We will then be logged in to the machine if we get mininet@mininet-vm:∼$.
We will be needing an X server and a SSH client. X server is necessary inorder to assign IP to the host and SSH client is necessary for making a remote connection which in our case is accessing virtual machine from host machine (Windows). We have used Xming as X server and PuTTy as SSH client. Firstly we need to run xming which once run can be seen on the notiﬁcation panel of the taskbar. Now in the virtual console of the virtual machine i.e. mininet@mininet-vm:∼$ type sudo ifconﬁg -a to view all the network adapters. There we will see eth1 which we had setup earlier while conﬁguring the virtual machine. This port is initially not assigned with any IP. Now inorder to assign it with an IP address we type : $ sudo dhclient eth1. This will assign IP to the port which is done by Xming. Now we need to SSH from host machine to virtual machine (remote).
We can SSH using PuTTy in windows considering following steps :
1. Download putty.exe and place it in your desired location in windows.
2. Open up command prompt.
3. Direct to the folder where you have kept putty.exe
4. In the command prompt type putty.exe -X user@IP-address-assigned-by-Xming-server Eg: putty.exe -X mininet@192.168.101.56
5. A SSH client window will open-up which is basically the interface to remote machine we are connecting to.
Now we can create simple network topologies in mininet using a basic command sudo mn. For more speciﬁc ones we can give arguments in the command. For eg ::∼$sudo mn –topo single,3 –mac –switch ovsk –controller remote
where,
sudo provides administrative priviledge 
mn starts basic mininet software script
–topo is the python function inside the script single is for linear topology 
3 means 3 hosts 
–mac deﬁne easy mac address 
ovsk means the topology is using openV switch

For our case we will create a simple network topology having 2 hosts connected to a single switch and the switch connected to the controller. For this we simply use :∼$ sudo mn. Once we hit enter it will show the setting up part and then we will enter to mininet CLI. In the CLI we can use diﬀerent commands like mininet>nodes which will show us the nodes in the network topology. Information about other commands can be gained using help command.
Now since the network topology we setup has two hosts h1 and h2, for implementation of Cristian‘s algorithm we need to make one as time-server and another as client/host. Check the IP address of any one of the host which we intend to make timeserver. For this case we have considered h1 to be time-server, so we need to enter the command mininet>h1 ifconﬁg. This will tell us the IP address of the host h1 which we need to place in the server.py script inorder to create a socket. Now we perform a quick ping test using pingall command inorder to check if h1 and h2 can communicate or not. If the communication is possible we now open up terminals of both h1 and h2 using xterm command i.e. mininet>xterm h1 h2. Both h1 and h2 have a pound sign (:∼#) indication we have root privileges. Now using nano editor we type in the server and client script and save them in respective hosts. For that purpose use :∼# nano server.py and after typing the code save it. Similar is the case for client.py. Now in h1 host we run the server.py script using command :∼# python server.py which is listening on port 9999. On the terminal of h2 host we run the client.py script with similar command. Once the client connects to the port 9999 on which the server is listening to the server will send the client the current time and in the client process we have implemented Cristian‘s algorithm inorder to add up the request and response time so that the client can get the actual time and not the delayed one.
After implementation of the algorithm we can stop the processes by closing the terminals of h1 and h2 and exit out of mininet using command mininet>exit. To clear out the topology created earlier we use the command sudo mn -c.
