""" Script to print out local ip and public ip"""
import socket
import requests


def get_internet_ip():
    ip = requests.get("https://ipv4bot.whatismyipaddress.com/").text
    return ip


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('1.1.1.1', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == "__main__":
    my_local_ip = get_local_ip()
    my_internet_ip = get_internet_ip()
    print("Local ip:", my_local_ip, "Public ip:", my_internet_ip)
