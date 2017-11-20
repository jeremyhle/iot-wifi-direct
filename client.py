import socket, os, random, sys, datetime

# generates a random temperature from 0 to 100 Celcius
def generateTemp():
    return random.randrange(0, 101)

# sends temperature to server
def sendTemp(clientsocket):
    freq = 5
    while freq > 0:
        intTemp = generateTemp()
        temperature = str(intTemp)
        if (intTemp > 30):
            clientsocket.sendall(temperature)
            print "Temperature sent: {} Celcius".format(temperature)
            getTimestamp()
        freq -= 1
    clientsocket.close()

# sends an image to server
def sendImage(clientsocket):
    filename = '/home/jeremy/Desktop/star-tree/wifi-direct/test.png'
    f = open(filename, 'rb')
    l = f.read(1024)
    while l:
        clientsocket.send(l)
        l = f.read(1024)
    clientsocket.close()
    
############################################
# Functions used for collecting data
############################################

def getTimestamp():
    print datetime.datetime.now()


#establish connections with host and port
host = 'localhost'
port = 12345

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))


sendTemp(clientsocket)
#sendImage(clientsocket)

clientsocket.close()





