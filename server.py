import sys
import socket

def server():
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, 12345))

    s.listen(5)
    while True:
        conn, addr = s.accept()
        message = conn.recv(1024)
        print(message)
        conn.send(message)
        conn.close()

    

if __name__ == "__main__":
    server()