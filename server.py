import socket

def server():
	
    # ////////////////////////////  BIND AND LISTEN  ////////////////////////////////////
    s = socket.socket()         
    host = socket.gethostname() 
    s.bind((host, 12345))
    s.listen(5)

    while True:
        conn, addr = s.accept() # BEGIN CONNECTION
        
        # message = b''
        # while True:
        #     data = conn.recv(1)
            
        #     if data == b'':
        #         break
        #     if data ==  b'\n':
        #         break
                
        #     message += data

        message = parse_request(conn)

        print(message)
        conn.send(message)
        return(message)
        conn.close()     

        if message.decode() == 'q':
            break

def parse_request(socket):
    parse_head(socket)
    parse_body(socket)

def parse_head(socket):
    while get bytes
        break on CRLF
    expect CRLF

def parse_body(socket):
    while get bytes:
        break on CRLF
    expect CRLF

server()