import sys
import socket
from datetime import datetime

#sys.argv is [arg1,arg2], thats why len(sys.argv)==2 is used
if len(sys.argv) == 2:
    #translates the hostname to IPv4, picks the 2nd element in the array
    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid amount of argument")

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:

    #will scan ports between 1-1025
    for port in range(1,1025)
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        #return an error
        result = skt.connect_ex((target,port))
        if result==0:
            print("port {} is open".format(port))
        skt.close()

except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\nServer not responding !!!!")
        sys.exit()