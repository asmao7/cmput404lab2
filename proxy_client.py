import socket
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "Get / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    try:
        #create a tcp socket and connect
        s = soscket.socket(socket.AF_INET, soscket.SOCK_STREAM)(
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)

        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()
    
def main():
    connect(('127.0.0.1', 8001))

if __name__ == "__main__":
    main()