from scapy.all import *
import random
import numpy as np
import hashlib
from datetime import datetime
from sklearn.metrics import f1_score
import coordenador
import valores
import time
import resource
import os

pipesTable = np.array([np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,)], dtype=int)  
acumuladorPipe = np.zeros((524288,), dtype=int)
todosValoresHash = np.zeros((524288,),dtype=int)
controllerCheck = np.zeros((524288,),dtype=int)
pipeLimitArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

nSwitches = valores.qntDeSwitches()
globalLimit = valores.limiteGlobal()
nPipes = valores.qntDePipes()
#nPipes = 8
switchLimit = int(globalLimit/nSwitches)
switchLimitBackup = switchLimit
fluxoEmUmPipe = 0
hash = 0
hh = 0
xDict = 0
cont = 0
dict = {}
reports = 0
pipeLimit = int(switchLimit/nPipes)
randomPipe = random.randint(0,(nPipes-1))
switch = 1
fim = 0

#controla qual o limite de cada PIPE
def divisionLimitPipes():
    global switchLimit

    pipeLimitRest = (switchLimit % nPipes)

    if(pipeLimitRest==0):
        for i in range(len(pipeLimitArray)):
            pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==2) and (pipeLimitRest==1)):
        pipeLimitArray[0] = int(switchLimit/nPipes)
        pipeLimitArray[1] = int(switchLimit/nPipes) + 1 

    elif((nPipes==4) and (pipeLimitRest==1)):
        for i in range(len(pipeLimitArray)):
            if(i==3):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((nPipes==4) and (pipeLimitRest==2)):   
        for i in range(len(pipeLimitArray)):
            if(i>=2):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==4) and (pipeLimitRest==3)):   
        for i in range(len(pipeLimitArray)):
            if(i>=1):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==8) and (pipeLimitRest==1)):
        for i in range(len(pipeLimitArray)):
            if(i==7):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==8) and (pipeLimitRest==2)):
        for i in range(len(pipeLimitArray)):
            if(i>=6):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==8) and (pipeLimitRest==3)):
        for i in range(len(pipeLimitArray)):
            if(i>=5):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)    

    elif((nPipes==8) and (pipeLimitRest==4)):
        for i in range(len(pipeLimitArray)):
            if(i>=4):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==8) and (pipeLimitRest==5)):
        for i in range(len(pipeLimitArray)):
            if(i>=3):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
                
    elif((nPipes==8) and (pipeLimitRest==6)):
        for i in range(len(pipeLimitArray)):
            if(i>=2):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
                
    elif((nPipes==8) and (pipeLimitRest==7)):
        for i in range(len(pipeLimitArray)):
            if(i>=1):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif(nPipes==16):
        divisionLimitPipes2()

#controla qual o limite de cada PIPE
def divisionLimitPipes2():
    global switchLimit

    pipeLimitRest = (switchLimit % nPipes)

    if(pipeLimitRest==0):
        for i in range(len(pipeLimitArray)):
            pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((pipeLimitRest==1)):
        for i in range(len(pipeLimitArray)):
            if(i==15):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==2)):   
        for i in range(len(pipeLimitArray)):
            if(i>=14):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==3)):
        for i in range(len(pipeLimitArray)):
            if(i>=13):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==4)):   
        for i in range(len(pipeLimitArray)):
            if(i>=12):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==5)):
        for i in range(len(pipeLimitArray)):
            if(i>=11):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==6)):   
        for i in range(len(pipeLimitArray)):
            if(i>=10):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==7)):
        for i in range(len(pipeLimitArray)):
            if(i>=9):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==8)):   
        for i in range(len(pipeLimitArray)):
            if(i>=8):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==9)):
        for i in range(len(pipeLimitArray)):
            if(i>=7):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==10)):   
        for i in range(len(pipeLimitArray)):
            if(i>=6):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==11)):   
        for i in range(len(pipeLimitArray)):
            if(i>=5):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==12)):   
        for i in range(len(pipeLimitArray)):
            if(i>=4):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((pipeLimitRest==13)):   
        for i in range(len(pipeLimitArray)):
            if(i>=3):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((pipeLimitRest==14)):   
        for i in range(len(pipeLimitArray)):
            if(i>=2):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==15)):   
        for i in range(len(pipeLimitArray)):
            if(i>=1):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

#cria o hash e pega a origem e destino do fluxo
def createHash(packet):

    global fluxoEmUmPipe
    global hash
    global randomPipe
    global switchLimit

    if (fluxoEmUmPipe < int((switchLimit/2))):
        fluxoEmUmPipe = fluxoEmUmPipe + 1
    else:      
        randomPipe = random.randint(0,(nPipes-1)) 
        fluxoEmUmPipe = 0
 
    #seleciona a origem e destino do pacote IP 
    if IP in packet and TCP in packet:
        ip_src=packet[IP].src
        ip_dst=packet[IP].dst
        tcp_sport=packet[TCP].sport
        tcp_dport=packet[TCP].dport
        hash = int(hashlib.md5((str(ip_src) + str(ip_dst) + str(tcp_sport) + str(tcp_dport)).encode()).hexdigest(), 16) % 524288
        concatenadoIP = str(ip_src)+str(ip_dst)+str(tcp_sport)+str(tcp_dport)

        #contador de pacotes na posição da tabela hash 
        pipesTable[randomPipe][hash] = pipesTable[randomPipe][hash] + 1
        todosValoresHash[hash] = todosValoresHash[hash] + 1

        checkLimit(randomPipe)
   
#checar se a contagem atingiu o limite
def checkLimit(randomPipe):

    global reports
    global switch
    global globalLimit
    global switchLimit
    global switchLimitBackup    
    global fim

    if (pipesTable[randomPipe][hash] == pipeLimitArray[randomPipe]):
        acumuladorPipe[hash] = acumuladorPipe[hash] + pipesTable[randomPipe][hash]
        pipesTable[randomPipe][hash] = 0
    
        if (acumuladorPipe[hash]>=switchLimit):
            total = acumuladorPipe[hash]
            #coordenador.funcaoCoordenadorA(hash,total,switch,switchLimit,fim) #Para limite fixo utilizar essa linha

            #Para limite adaptativo utilizar esse bloco
            #'''
            switchLimit = coordenador.funcaoCoordenadorA(hash,total,switch,switchLimit,fim) 
            if(switchLimit!=switchLimitBackup):
                divisionLimitPipes()
                divisionLimitPipes2()             
                #print("\nSwitch",switch)
                print("...")
                print("Limite anterior",switchLimitBackup)
                switchLimitInt = int(switchLimit)
                switchLimit = switchLimitInt
                print("Limite atual",switchLimit)
                switchLimitBackup = switchLimit                
            #'''
            reports = reports + 1
            acumuladorPipe[hash] = 0
        

def pegaAcumulador():
    global acumuladorPipe

    return acumuladorPipe

def pegaResiduos():
    global pipesTable
    
    return pipesTable

def main():

    inicio = time.time()
    global hh
    global reports
    global switch
    global pipesTable
    global controllerCheck
    global acumuladorPipe
    global switchLimit
    global fim

    print("Switch 1 iniciado")
    print("Quantidade de pipes:", nPipes)
    now = datetime.now()
    divisionLimitPipes()     

    #leitura fluxo CAIDA
    sniff(offline="equinix-nyc-01.pcap", filter = "ip and tcp", prn=createHash, store = 0)
    fim = 1
    coordenador.controllerSwitchA(acumuladorPipe, controllerCheck, pipesTable, reports, switch,switchLimit,fim)
    fimTempo = time.time()
    tempo_execucao = fimTempo - inicio
    tempo_formatado = "{:.2f}".format(tempo_execucao)

    print("Tempo de execução Switch 1:", tempo_formatado, "s")
    print("\n")
    
if __name__ == '__main__':
    main() 
