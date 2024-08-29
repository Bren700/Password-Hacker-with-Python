import socket
import sys


with socket.socket() as cs:
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    data = sys.argv[3]

    address = (hostname, port)
    cs.connect(address)

    data = data.encode()
    cs.send(data)

    response = cs.recv(1024)
    print(response.decode())