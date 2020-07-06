#!/usr/bin/env python3

import sys
import socket
from datetime import datetime


def port_scan():
    """Basic Port scanner, scans ports between 50-85 for faster results.
    """
    try:
        if len(sys.argv) == 2:
            if len(sys.argv[1].split(".")) == 4 and socket.inet_aton(sys.argv[1]):
                # Translate hostname to IPV4
                target = socket.gethostbyname(sys.argv[1])
                print("=" * 50)
                print("Scanning target", target)
                print("Time Started: ", str(datetime.now()))

                for port in range(50, 85):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((target, port))  # returns an error indicator
                    if result == 0:
                        print(f"Port {port} is open.")
                    s.close()

                print("Finished Scanning", str(datetime.now()))
            else:
                print("Ip adress not valid. (###.###.###.###)")

        else:
            print("Invalid number of arguments.")
            print("Syntax: python3 port_scanner.py <ip>")

    except socket.error as err:
        print("Socket error:", err)
        sys.exit()
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()


if __name__ == "__main__":
    port_scan()
