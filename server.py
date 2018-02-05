import socket
import re

status = "200 OK"

def change_status():
    status = "500 INTERNAL SERVER ERROR"
    return status

def server():
	
    # ////////////////////////////  BIND AND LISTEN  ////////////////////////////////////
    s = socket.socket()         
    host = socket.gethostname() 
    s.bind((host, 12345))
    s.listen(5)

    while True:
        conn, addr = s.accept() # BEGIN CONNECTION

        try:
            message = parse_request(conn) # ASSEMBLE MESSAGE AS "MESSAGE" IN SERVER
        except: 
            change_status()

        print(message[1], message[0], status)

        msg = str.encode(message[1] + message[0] + status)
        # conn.sendall(msg) # SEND MESSAGE BACK
        return(message, status)

# ////////////////////////////  INITIALIZE PARSE FUNCTIONS  ////////////////////////////////////
def parse_request(socket):

    data = read(socket)
    return(parse_head(socket, data), parse_body(socket, data))

# ///////////////////////  RETURN HEAD VALUES  ///////////////////////////////
def parse_head(socket, data):

    message = data.decode()
    message = re.search('/r/n/r/n(.*)/r/n/r/n', message)
    return message.group(1)

# ////////////////////////  RETURN BODY VALUES  /////////////////////////
def parse_body(socket, data):

    message = data.decode()
    message = message[0:message.find('/r/n/r/n')]
    return message

# /////////////////////////////////// READ BINARY DATA //////////////////////////////////////
def read(socket):

    message = b'' # MARK MESSAGE TO BE INTERPRETED AS BINARY
    while True:
        data = socket.recv(1) # ITERATE THROUGH MESSAGE ONE BYTE AT A TIME

        if data == b'':
            break
        if data == b'\n':
            break

        message += data # ASSEMBLE MESSAGE

    return message

server()