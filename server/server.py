"""
Server receiver of the file
"""
import socket
#import tqdm
import os

# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = int(os.environ.get('PORT', 5000))
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
# create the server socket
# TCP socket
s = socket.socket()
# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))
# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# accept connection if there is any
client_socket, address = s.accept()
# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.")

# receive the file infos
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
print(received)
filename, filesize, fileid = received.split(SEPARATOR)
filename = filename.split('.')[0]
print(fileid)
# remove absolute path if there is
'''filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)'''
# start receiving the file from the socket
# and writing to the file stream
#progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(fileid+".py", "wb") as f:
    while True:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        # print(bytes_read)
        if not bytes_read:
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        # progress.update(len(bytes_read))

#os.system('python ' + fileid + ".py")
otp = os.popen('python ' + fileid + ".py").read()

'''
queue = []
while True:
    if count <= 10:
        otp = os.popen('python ' + fileid + ".py").read()
        count += 1
    else:
        
'''
#print(type(otp), otp)

# close the client socket
client_socket.close()
# close the server socket
s.close()
