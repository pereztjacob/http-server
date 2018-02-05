import sys
import socket

s = socket.socket()
host = socket.gethostname() 

def client(message):
# ////////////////////  CONNECT  ////////////////////////////////////////////////////////
    try:
        s.connect((host, 12345))
    except:
        print("Connection Failed")
    else:
        msg = str.encode(message) # TURN TO BINARY
        s.sendall( msg ) # SEND TO SERVER
        print(message)
        var = read(s)

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

    client(full) # CALL CLIENT FOR (MESSAGE)

def read(conn):
    recov = b''
    try:
        # data = conn.recv(1)
        pass
    except:
        print('failed to retrieve data')
        return
    # else:
    #     print('data: ', data)
    
    # recov += data

    return recov









	
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: client EOM message")
    else:
        make_request('hello world')