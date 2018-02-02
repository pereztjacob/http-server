import sys
import socket

def client(eom, message):

    s = socket.socket()

    host = socket.gethostname() 

    try:
        s.connect( ( host, 12345 ) )
    except:
        print("Connection Failed")
    else:
        msg = str.encode(message) 

        s.sendall( msg )

        if eom == "close":
            print(message)
            s.close()
            return
        elif eom == "LF":
            s.send(str.encode("\n"))

        raw = s.recv(len(message))

        result = raw.decode()

        
        s.close()

        if result == message:
            print("OK: got echo")
            return True
        else:
            print("FAILED: got some other message: " + result)
            return False	
	
if __name__ == "__main__":
	if len(sys.argv) <= 2:
		print("Usage: client EOM message")
	else:
		client(sys.argv[1], sys.argv[2])