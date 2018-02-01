import sys
import socket

def client(message):
    s = socket.socket()
    host = socket.gethostname()
    res = socket.gethostbyaddr("127.0.0.1")
    host = res[0]

    try:
        s.connect((host, 12345))
    except:
        print("connection failed")
    else:
        s.send(str.encode(message))
        gett = s.recv(len(message))
        result = gett.decode()
        if(result == message):
            print('go ahead', message)
        s.close()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('not good')
    else:
        client(sys.argv[1])