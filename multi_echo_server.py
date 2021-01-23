import socket, sys
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)
        while True:
            conn, addr = proxy_start.accept()
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started process ", p)

    def handle_echo(addr, conn):
        print("connected by", addr)

        full_data = conn.recv(BUFFER_SIZE)
        conn.sednall(full_data)
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

if __name__ == if __name__ == "__main__":
    :
    main()