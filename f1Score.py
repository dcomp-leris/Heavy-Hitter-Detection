from scapy.all import *
import random
import time
import numpy as np
import hashlib
from datetime import datetime
from sklearn.metrics import f1_score
import coordenador
import valores

nSwitches = 1
globalLimit = valores.limiteGlobal()
nPipes = valores.qntDePipes()
switchLimit = int(globalLimit/nSwitches)
hash = 0
hh = 0
xDict = 0
cont = 0
dict = {}

def createHash(packet):
    
    global hash

    if IP in packet and TCP in packet:
        ip_src=packet[IP].src
        ip_dst=packet[IP].dst
        tcp_sport=packet[TCP].sport
        tcp_dport=packet[TCP].dport
        concatenadoIP = str(ip_src)+str(ip_dst)+str(tcp_sport)+str(tcp_dport)
        createHashDict(concatenadoIP)

def createHashDict(concatenadoIP):
    global cont
    global xDict

    cont = 0

    if concatenadoIP in dict:
        cont = (dict.get(concatenadoIP))
        cont = cont + 1
        dict[concatenadoIP] = (cont)
    else:
        dict[concatenadoIP] = (1)
    xDict = xDict+1

def checkLimitDict():

    i = 0
    hhDict=0
    x=0
    hashPrint=0
    
    array=list(dict.values())
    arrayKey=list(dict.keys())

    for x in range(len(array)):
        if(array[x]>=globalLimit):
            hashPrint = int(hashlib.md5((arrayKey[x]).encode()).hexdigest(), 16) % 524288
            #print("->>" ,hashPrint, " ",array[x])
            hhDict = hhDict+1
    return hhDict

def main():

    inicio = time.time()
    global hh
    global xDict
    vp = 0
    vn = 0
    fp = 0
    fn = 0

    #print("Contagem Dicionario") 

    #leitura fluxo CAIDA
    sniff(offline="equinix-ncy.pcap", filter = "ip and tcp", prn=createHash, store = 0)
    hhDict = checkLimitDict()
    print("\\\\\HH do Dicionario:",hhDict) 
    print("\n\n--------------------------------")

    #Obtem a tabela final dos hashes para comparar e realizar o F1-Score
    tabelaCoordenador = coordenador.f1score()
    for chave in dict.keys():
        
        hash = int(hashlib.md5((str(chave)).encode()).hexdigest(), 16) % 524288
       
        if((dict[chave]<=globalLimit) and (tabelaCoordenador[hash]<=globalLimit)):
            vn = vn+1
        elif((dict[chave]>=globalLimit) and (tabelaCoordenador[hash]>=globalLimit)):
            vp = vp +1
        elif((dict[chave]<=globalLimit) and (tabelaCoordenador[hash]>=globalLimit)):
            fp = fp +1    
        elif((dict[chave]>=globalLimit) and (tabelaCoordenador[hash]<=globalLimit)):
            fn=fn+1
            

    print("Cálculo F1 Score")
    print("\n")
    print("VP=",vp)
    print("VN=",vn)
    print("FP=",fp)
    print("FN=",fn)
    print("\n")

    qhh = coordenador.qHH()

    if(hhDict>0):
        precision = vp/qhh 
    elif(hhDict<0):
        precision=0    
    recall = vp / (vp + fn)
    f1Score = (2 * (precision * recall)) / (precision + recall) 

    print("-Precision:",precision)
    print("-Recall:",recall)
    print("-F1Score:",f1Score)
    print("\n")

    fim = time.time()
    tempo_execucao = fim - inicio
    print("Quantidade de pacotes:",xDict)
    print("Quantidade de fluxos:",(len(dict)))
    print("Tempo de Execucao:", tempo_execucao)
    

if __name__ == '__main__':
    main()   
