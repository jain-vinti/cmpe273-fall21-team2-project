import socket
#import tqdm
import os
import random

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step# the ip address or hostname of the server, the receiver
host = "localhost"
# the port, let's use 5001
port = 5001
# the name of file we want to send, make sure it exists
filename = "test.py"
# get the file size
filesize = os.path.getsize(filename)
fileid =str(random.randint(1111,9999))
print(fileid)
# create the client socket
s = socket.socket()
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{fileid}".encode())
# start sending the file
#progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        print(bytes_read)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        #progress.update(len(bytes_read))
# close the socket
s.close()