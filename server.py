import socket

def server():
	
    s = socket.socket()         

    host = socket.gethostname() 

    s.bind((host, 12345))

    s.listen(5)

    while True:
        conn, addr = s.accept()
        
        message = b''
        while True:
            data = conn.recv(1)
            
            if data == b'':
                break
            if data ==  b'\n':
                break
                
            message += data

        print(message)
        conn.send(message)
        return(message)
        conn.close()     

        if message.decode() == 'q':
            break

server()