# port_scanner
A simple python port scanner
-------------------------------------------------------------------------------------
A script for scanning open ports in a network.
Run it in you favorite shell to scan for open ports.

Usage Example: python scanner.py 192.168.0.1 20 65 
Syntax: python scanner.py [ip address or hostname] [start port] [end port]

*Depending on your system or version of python the first keyword may vary.
It works for me with "python" but might as well be "-m python" or "python3"

*hostname have to be recognized by your network in order to be resolved. 
If it doesnt work use ip address instead.

I haven't added IP address validation yet so it will accept invalid octets and crash.
======================================================================================
!!! Please use it responsibly: to protect not to harm systems.
======================================================================================
