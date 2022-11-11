import socket
#create a socket object
sclient = socket.socket()

#cross-platform, telnet-ish connection
PORT = 12345
HOST = socket.gethostbyname('localhost')

#in order to connect to a server - i must connect to its socket
sclient.connect((HOST, PORT))

#receive some data from our connected cleints (decode that string)
print(sclient.recv(1024).decode())
print(sclient.recv(1024).decode())

while True:
    #message = input()
    message = sclient.recv(1024)
    message = message.decode()
    print("From server", ">", message)
    message = input(str("Me client > "))

    if message == "[bye]":
        message = "Leaving the Chat room"
        sclient.send(message.encode())
        print("\n")
        break
    sclient.send(message.encode())

#close connection
sclient.close()