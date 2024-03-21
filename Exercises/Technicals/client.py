from socket import socket
from sys import *

def main():
    serveur = socket()
    try:
        argv[1] = int(argv[1])
    except:
        print("USAGE : python3 server.py [port]")
        return
    serveur.connect(('', int(argv[1])))
    phrase = input() + "\n"
    while phrase != "END\n":
        serveur.send(phrase.encode())
        phrase = input() + "\n"
    serveur.send(phrase.encode())
    serveur.close()

if __name__ == '__main__':
    main()