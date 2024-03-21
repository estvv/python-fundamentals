from socket import socket
from sys import *

def main():
    serveur = socket()
    try:
        argv[1] = int(argv[1])
    except:
        print("USAGE : python3 server.py [port]")
        return
    try:
        serveur.bind(('', argv[1]))
    except OSError:
        print(":D")
    print("Server started!")
    print("Waiting for clients...")
    serveur.listen()
    while True:
        (sclient, adclient) = serveur.accept()
        print("Connexion from ...", adclient)
        donnees = sclient.recv(1024)
        while donnees:
            print(donnees.decode(), end='')
            donnees = sclient.recv(1024)
            if donnees.decode() == "END\n":
                print("Deconnexion ", adclient)
                break
        sclient.close()

if __name__ == '__main__':
    main()