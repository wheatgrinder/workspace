# load additional Python modules
import socket  
import time
from datetime import datetime
import sys



print(sys.argv[1])
# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)

# bind the socket to the port 23456, and connect
server_address = (ip_address, 23456)  
sock.connect(server_address)  
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))


#while ch < 0:
try:
    while 1:
        sock.open()
        #sock.connect(server_address)  
        #print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))
        # define example data to be sent to the server
        #timestaped_data = str(time.time()).encode("utf-8")
        #sock.sendall(timestaped_data)
        dt = datetime.now()
        #sock.sendall(dt.microsecond)
        data = str(dt.microsecond).encode("utf-8")
        timestaped_data = str(sys.argv[1] + ":" + str(dt.microsecond)).encode("utf-8")
        sock.sendall(timestaped_data)
        #sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        time.sleep(2)
        

except KeyboardInterrupt:
    # close connection
    print("close connection:")
    sock.close()  