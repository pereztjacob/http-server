import sys
import socket

s = socket.socket()
host = socket.gethostname() 

def client(eom, message):

# ////////////////////  CONNECT  ////////////////////////////////////////////////////////
    try:
        s.connect((host, 12345))
    except:
        print("Connection Failed")
    else:
        msg = str.encode(message) # TURN TO BINARY

        s.sendall( msg ) # SEND TO SERVER

        if eom == "close":
            print(message)
            s.close()
            return
        elif eom == "LF":
            s.send(str.encode("\n"))

        raw = s.recv(len(message)) # RECIEVE FULL MESSAGE

        result = raw.decode()
        print(result)

        s.close()

# //////////////////////////  ASSEMBLING MESSAGE  /////////////////////////////////////
def make_request(message):
    REQUEST = "GET"
    VERSION = "HTTP/1.1"
    CRLF    = "/r/n"

    request = REQUEST + " " + VERSION + CRLF
    headers = "Host: {0}".format(host) + CRLF
    head = request + headers
    body = message + CRLF
    full = head + CRLF + body + CRLF

    client('close', full) # CALL CLIENT FOR (MESSAGE)

def parse_response():
    while get bytes
        break on CRLF
	
if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Usage: client EOM message")
    else:
        # client(sys.argv[1], sys.argv[2])
        response_ok('hello world')