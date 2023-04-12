#!/bin/bash

import sys
import socket
from datetime import datetime as dt

# defining target
if len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1]) #translates host name to IPv4
else:
    print('Invalid number of arguments') # had to add IP validation later
    print('Syntax: python3 scanner.py [ip address/host name] [start port] [end port]')
    sys.exit()

# adding user confirmation
print('-'* 50)
print(f'Scanning target {target}')
print(f'Time started: {str(dt.now())}')
print('-'* 50)

try:
    for port in range(int(sys.argv[2]), int(sys.argv[3])):
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = serv.connect_ex((target, port))
        if result == 0:
            print(f'Port {port} is open')
        serv.close()
except KeyboardInterrupt:
    print('\n Exiting scan...')
    sys.exit()
except socket.gaierror:
    print('Host name cannot be resolved.')
    sys.exit()
except socket.error as err:
    print(f'Could not connect to server. Error: {err}')
    sys.exit()