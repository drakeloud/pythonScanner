#!/usr/bin/python


from os import system, name
import sys
import argparse
import subprocess
import socket
from datetime import datetime
from netaddr import IPNetwork

# Set up argparse
parser = argparse.ArgumentParser()
parser.add_argument("hosts")
parser.add_argument("ports")
parser.add_argument("-u", "--UDP", help="Perform a UDP scan on the ports specified", action="store_true")
parser.add_argument("-t", "--traceroute", help="Use traceroute with the scan", action="store_true")
args = vars(parser.parse_args())

# Clean the shell window for better UI
subprocess.call('clear', shell=True)

# Start timer! woo hoo!
time_one = datetime.now()

# Clean the ports that you received
ports_ugly = args['ports']
ports = ports_ugly.split(",")
UDP = args['UDP']
host_value = args['hosts']
hosts = []


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


clear()
print("*************************************************************************")
print("                    Scanning hosts, please wait...")
print("*************************************************************************")
print("")
print("User entered ports: ", ports_ugly)
print("")
print("User entered hosts: ", host_value)
print("")
if UDP:
    print("Currently Scanning UDP ports...")
else:
    print("Currently Scanning TCP ports...")
print("")

# Get Hosts Values
if "/" in host_value:
    ip = IPNetwork(host_value)
    ip_list = list(ip)

    for ip in IPNetwork(host_value).iter_hosts():
        hosts.append('%s' % ip)

else:
    hosts.append(host_value)

# Function to get the ports for every host


def scan_ports(port_host):
    try:
        for port in ports:
            # Goes through each port in range
            port = int(port)
            # Here's the scan of the port
            if UDP:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            result = sock.connect_ex((port_host, port))

            if UDP:
                if result == 0:
                    print(f"UDP Port {port}: \t Open")
            else:
                if result == 0:
                    print(f"TCP Port {port}: \t Open")
            sock.close()

    # Error handling if something goes bad
    except socket.gaierror:
        print("Couldn't find hostname. The hostname may be invalid or incorrect.")
        sys.exit()

    except socket.error:
        print('Bad connection to server. Try again later.')
        sys.exit()


print("----------------RESULTS----------------")
for host in hosts:

    print("Scanning host: ", host)

    scan_ports(host)
    print("")

timeTwo = datetime.now()

finalTime = timeTwo - time_one
print("Scan finished in the following time: ", finalTime)
print("*************************************************************************")
print("                Hosts Scanned. Finishing up... (-.-)Zzz...")
print("*************************************************************************")
