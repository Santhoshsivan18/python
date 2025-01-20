# Server
"""
import socket

s = socket.socket()
print("Socket created successfully")
port = 50050  # 0-1023(BIOS), 1024-49151(UserImportApps), 49152-65535
s.bind(("192.168.29.230", port))
print("Socket binded to %s" %(port))
s.listen(5) # 5 times they can communicate(not related to time but no.of requests)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print("Got connection from ", addr)
    c.send(b'Thanks for connecting!!!!') # send in binary format for loseless transmission
    c.close()
"""
# Client
# goto cmd -> type python -> copy & paste following code
"""
import socket
s = socket.socket()
port = 50050
s.connect(("192.168.29.230", port))
print(s.recv(1024))
s.close()
"""


# FTP server

import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    # Instantiate a dummy auth for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # perm="elradfmwMT" give this only for users that need to have read-only access
    # if this perm="elradfmwMT" is not given all permissions are enabled
    # Define a new user having full r/w permissions & a read-only access
    authorizer.add_user("user", "1234", ".", perm="elradfmwMT")
    # authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connected)
    handler.banner = "FTP is ready"

    # Specify a masquerade address & the range of ports to use for passive connections
    # Uncomment the next 2 lines if behind a NAT
    # handler.masquerade_address = "151.25.42.11"
    # handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class & listen on 0.0.0.0.:2121
    address = ("192.168.29.230", 21)  # 21 is the file reading port so don't change it
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 250
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()


if __name__ == "__main__":
    main()

"""
open cmd as admin
type ftp
ftp>open
ip addr 21
user
passwd
get <file>
"""