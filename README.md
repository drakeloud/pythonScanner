# pythonScanner
Python Scanner for running TCP or UDP scans on python 2.7

Installation:

1. pip install netaddr
2. Make the python script an executable
3. Scan!

Usage:
The script takes arguments in this fashion:
./pythonScanner ipaddress ports optionalFlags

If you want to run several ip addresses, then use CIDR notation. E.g.
./pythonScanner 192.168.1.1/28 80

If you want to run several ports, simply separate the ports with a comma. E.g.
./pythonScanner 192.168.1.1/28 21,22,25,53,80

By default, TCP ports are scanned but by using the UDP flag, it will scan UDP, not TCP. E.g.
./pythonScanner 192.168.1.1/28 21,22,25,53,80 -u

If you are lost, just check out the help menu! E.g.
./pythonScanner -h

Good luck! and happy scanning!
