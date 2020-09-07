import socket
dir = "directory to file of DNS names"
with  open (dir, "r") as ins:
    for line in ins:
        print(socket.gethostbyname(line.strip()))