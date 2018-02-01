import sys
import socket
import http.client

def client(message,resp=False):
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

def test_response():
    host = 'www.google.com'
    directories = ['aosicdjqwe0cd9qwe0d9q2we', 'reader', 'news']

    for directory in directories:
        conn = http.client.HTTPConnection(host)
        conn.request('HEAD', '/' + directory)

        url = 'http://{0}/{1}'.format(host, directory)

        response = conn.getresponse()
        print(response.status, response.reason)

        conn.close()

test_response()

# def response_ok(host):
#     conn = http.client.HTTPConnection(host)
#     conn.request("HEAD")
#     return conn.getresponse().status

# print(response_ok("stackoverflow.com"))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('not good')
    else:
        client(sys.argv[1])