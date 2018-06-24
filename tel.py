# -*- coding: utf-8 -*-
from socket import *
#from sentence2vec import sentence2vec
import numpy as np
import sys
global connectionSocket
BUFSIZE = 1024

reload(sys)
sys.setdefaultencoding('utf-8')

def config():
    global connectionSocket
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('165.246.241.148', serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()
    print('accept!')
    print("log config: ", connectionSocket)
    return connectionSocket

def receive():
    global connectionSocket
    print("log receive: ",connectionSocket)
    tmp_sentence = str(connectionSocket.recv(1024)).encode("utf-8")
    tmp_1sentence = tmp_sentence.decode("utf-8").encode("utf-8")
    sentence = unicode(tmp_1sentence)
    # sentence=str(unicode(tmp_sentence))
    print("log: receive ", sentence)
    #connectionSocket.close()
    return sentence

def sending(IN):
    global connectionSocket
    #IN = input()
    connectionSocket.send(IN.encode('utf-8'))
    #connectionSocket.close()

def closeSocket():
    global connectionSocket
    connectionSocket.close()

if __name__=="__main__":
    connectionSocket=config()
    flag=True
    while(flag):
        try:
            sentence= str(connectionSocket.recv(1024)).encode("utf-8")
            print("log: tel.py: ",)
            print(sentence)
        finally:
            connectionSocket.close()

