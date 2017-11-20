#uses TCP/IP protocol

import socket, os, sys

#receives temperature from client
def receiveTemp(serversocket):
    freq = 5
    conn, addr = serversocket.accept()
    while 1:
        data = conn.recv(1024)
        if len(data) > 0:
            print "Temperature received: {} Celcius".format(data)
    conn.close()
    serversocket.close()

# receives an image from client
def receiveImage(serversocket):
    while 1:
        conn, addr = serversocket.accept()
        f = open('/home/jeremy/Desktop/receivedImg.png', 'wb')
        while 1:
            l = conn.recv(1024)
            while l:
                f.write(l)
                l = conn.recv(1024)
        f.close()
        conn.close()
    serversocket.close()

HOST = ''
PORT = 12345

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((HOST, PORT))
serversocket.listen(1)

receiveTemp(serversocket)

#receiveImage(serversocket)


