#!/usr/bin/python
from __future__ import print_function

import argparse
import os
import socket
import sys
from datetime import datetime

from netaddr import IPNetwork

# Set up argparse
parser = argparse.ArgumentParser()
parser.add_argument("hosts")
parser.add_argument("ports")
parser.add_argument("-u", "--UDP", help="Perform a UDP scan on the ports specified", action="store_true")
parser.add_argument("-t", "--traceroute", help="Use traceroute with the scan", action="store_true")
args = vars(parser.parse_args())

# Start timer! woo hoo!
timeOne = datetime.now()

# Clean the ports that you received
portsUgly = args['ports']
ports = portsUgly.split(",")
UDP = args['UDP']
hostValue = args['hosts']
hosts = []


def clear_screen():
    """
    Clear screen that handle multiple OS.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def scan_ports(host):
    """
    Function to get the ports for every host
    """
    try:
        for port in ports:
            # Goes through each port in range
            port = int(port)
            # Here's the scan of the port
            if UDP:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            result = sock.connect_ex((host, port))

            if UDP:
                if result == 0:
                    print("UDP Port {}: \t Open".format(port))
            else:
                if result == 0:
                    print("TCP Port {}: \t Open".format(port))
            sock.close()

    # Error handling if something goes bad
    except socket.gaierror:
        print('Couldnt find hostname. The hostname may be invalid or incorrect.')
        sys.exit()
    except socket.error:
        print('Bad connection to server. Try again later.')
        sys.exit()
    except KeyboardInterrupt:
        print('Bye..')
        sys.exit()


if __name__ == '__main__':
    clear_screen()
    print("*************************************************************************")
    print("                    Scanning hosts, please wait...")
    print("*************************************************************************")
    print("")
    print("User entered ports: ", portsUgly)
    print("")
    print("User entered hosts: ", hostValue)
    print("")
    if UDP:
        print("Currently Scanning UDP ports...")
    else:
        print("Currently Scanning TCP ports...")
    print("")

    # Get Hosts Values
    if "/" in hostValue:
        ip = IPNetwork(hostValue)
        ip_list = list(ip)

        for ip in IPNetwork(hostValue).iter_hosts():
            hosts.append('%s' % ip)

    else:
        hosts.append(hostValue)

    print("----------------RESULTS----------------")
    for host in hosts:
        print("Scanning host: ", host)
        scan_ports(host)
        print("")

    timeTwo = datetime.now()

    finalTime = timeTwo - timeOne
    print("Scan finished in the following time: ", finalTime)
    print("*************************************************************************")
    print("                Hosts Scanned. Finishing up... (-.-)Zzz...")
    print("*************************************************************************")
