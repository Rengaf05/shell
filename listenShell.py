import socket
import sys
import os

bind_host = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_host,bind_port))
server.listen(5)
print "[*] Server listening on %s:%d" % (bind_host,bind_port)

def sender(client):
    while True:
        try:
            cmd = raw_input(">")
            client.send(cmd + "\n")
            recv(client)
        except:
            sys.exit(0)
def recv(client):
    recv_len = 1
    response = ""

    while recv_len:
        try:
            data = client.recv(4096)
            recv_len = len(data)
            response += data

            if recv_len < 4096:
                break
        except KeyboardInterrupt:
            sys.exit(0)
    
    print response


# MAIN LOOP
while True:
    try:
        client,addr = server.accept()
    except KeyboardInterrupt:
        sys.exit(0)

    print "[*] Connection from %s:%d" % (addr[0],addr[1])
    sender(client)
