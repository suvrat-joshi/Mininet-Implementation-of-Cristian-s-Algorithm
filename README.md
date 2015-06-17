# Mininet-Implementation-of-Cristian-s-Algorithm
Clock synchronization is carried out using Cristian`s algorithm, coded as python script and which is implemented in Mininet which is used for network virtualization.

Initially we need to setup a virtual environment in our host operating system. For this purpose we need to download Virtualbox from https://www.virtualbox.org/ wiki/Downloads. There we ﬁnd diﬀerent binary releases for diﬀerent platform. Since we are working on windows platform we need to download <b>VirtualBox 4.3.28</b> the latest one for Windows hosts. Then we need to download mininet virtual image which we can get from https://github.com/mininet/openflow-tutorial/wiki/ Installing-Required-Software. There we select either 32bit or 64bit version. For our project we are using 32bit one which is <b>Virtual Machine Image (OVF format, 32-bit, Mininet 2.2.0)</b>. The OVF format can be imported into VirtualBox, VMware or other popular virtualization program. We can also install mininet using native installation from the source which is also present in the github repository.
Once downloaded, we need to setup virtualbox in our machine. After the installation process, we now run virtualbox. There we need to setup a virtual machine. The procedure is as follows :

  * On the top left corner of the window click on <b>New</b>.
  * Fill up the credentials by giving a <b>name</b> to the virtual machine, select <b>type</b> as Linux and <b>version</b> as 32bit.
  * Now provide a <b>memory size</b> for the virtual machine. You can leave this to default 512 MB.
  * On the next window choose <b>Use an existing virtual hard drive ﬁle</b> and browse to the folder where you downloaded the mininet virtual image.
  * Click on <b>Create</b> to create the speciﬁed virtual machine.

We also need to perform a quick conﬁguration before running the virtual machine. For that we need to follow the following steps :

  * Select the virtual machine on the left-hand panel of the virtual-box window.
  * Click on <b>Settings</b> and navigate to <b>Network</b> option.
  * Now click on <b>Adapter 2</b> tab and inside there check <b>Enable Network Adapter</b>.
  * Choose Attached to as <b>Host-only Adapter</b>.

This is necessary since we will be do a SSH from the host system (in our case Windows) to the virtual machine. After setting up the virtual machine run it. We will be prompted to virtual console where we need to enter the username and password inorder to access it. Enter username as ’mininet’ and password also as ’mininet’. We will then be logged in to the machine if we get 

```sh
  mininet@mininet-vm:∼$.
```

We will be needing an X server and a SSH client. X server is necessary inorder to assign IP to the host and SSH client is necessary for making a remote connection which in our case is accessing virtual machine from host machine (Windows). We have used <b>Xming</b> as X server and <b>PuTTy</b> as SSH client. Firstly we need to run xming which once run can be seen on the notiﬁcation panel of the taskbar. Now in the virtual console of the virtual machine i.e. 

```sh
  mininet@mininet-vm:∼$ sudo ifconﬁg -a
```

to view all the network adapters. There we will see eth1 which we had setup earlier while conﬁguring the virtual machine. This port is initially not assigned with any IP. Now inorder to assign it with an IP address we type

```sh
  :∼$ sudo dhclient eth1
```
This will assign IP to the port which is done by Xming. Now we need to SSH from host machine to virtual machine (remote).
We can SSH using PuTTy in windows considering following steps :

  * Download <b>putty.exe</b> and place it in your desired location in windows.
  * Open up command prompt.
  * Direct to the folder where you have kept putty.exe
  * In the command prompt type

```sh
  putty.exe -X user@IP-address-assigned-by-Xming-server
```
  Eg: putty.exe -X mininet@192.168.101.56
  * A SSH client window will open-up which is basically the interface to remote machine we are connecting to.

Now we can create simple network topologies in mininet using a basic command sudo mn. For more speciﬁc ones we can give arguments in the command. For eg :

```sh
  :∼$sudo mn –topo single,3 –mac –switch ovsk –controller remote
```

where, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sudo provides administrative priviledge<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mn starts basic mininet software script<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;–topo is the python function inside the script single is for linear topology<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 means 3 hosts<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;–mac deﬁne easy mac address<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ovsk means the topology is using openV switch

For our case we will create a simple network topology having 2 hosts connected to a single switch and the switch connected to the controller. For this we simply use 

```sh
  :∼$ sudo mn
```

Once we hit enter it will show the setting up part and then we will enter to mininet CLI. In the CLI we can use diﬀerent commands like <b>mininet>nodes</b> which will show us the nodes in the network topology. Information about other commands can be gained using help command.

Now since the network topology we setup has two hosts h1 and h2, for implementation of <b>Cristian‘s algorithm</b> we need to make one as time-server and another as client/host. Check the IP address of any one of the host which we intend to make timeserver. For this case we have considered h1 to be time-server, so we need to enter the command 

```sh
  mininet>h1 ifconﬁg
```

This will tell us the IP address of the host h1 which we need to place in the server.py script inorder to create a socket. Now we perform a quick ping test using pingall command inorder to check if h1 and h2 can communicate or not. If the communication is possible we now open up terminals of both h1 and h2 using xterm command i.e. 

```sh
  mininet>xterm h1 h2
```

Both h1 and h2 have a pound sign (:∼#) indication we have root privileges. Now using nano editor we type in the server and client script and save them in respective hosts. For that purpose use

```sh
  :∼# nano server.py
```

and after typing the code save it. Similar is the case for client.py. Now in h1 host we run the server.py script using command

```sh
  :∼# python server.py
  ```
  
which is listening on port 9999. On the terminal of h2 host we run the client.py script with similar command. Once the client connects to the port 9999 on which the server is listening to the server will send the client the current time and in the client process we have implemented Cristian‘s algorithm inorder to add up the request and response time so that the client can get the actual time and not the delayed one.
After implementation of the algorithm we can stop the processes by closing the terminals of h1 and h2 and exit out of mininet using command 

```sh
  mininet>exit
```

To clear out the topology created earlier we use the command 

```sh
  sudo mn -c.
```
