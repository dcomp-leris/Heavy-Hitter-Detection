import numpy as np
import valores
import switchA01
import switchA02
import switchA03
import switchLP01
import switchLP02
import switchLP03
import resource
import os

tabelaCoordenador = np.zeros((524288,), dtype=int)
heavyhitters = np.zeros((524288,),dtype=int)
nPipes = valores.qntDePipes()
somaReports = 0
hh=0
nSwitches = valores.qntDeSwitches()
globalLimit = valores.limiteGlobal()
alfa = valores.alfa()
contG1A = 0
contG2A = 0
contG3A = 0
contG1LP = 0
contG2LP = 0
contG3LP = 0
swLimitAnt1A = int(globalLimit/nSwitches)
swLimitAnt2A = int(globalLimit/nSwitches)
swLimitAnt3A = int(globalLimit/nSwitches)
swLimitAnt1LP = int(globalLimit/nSwitches)
swLimitAnt2LP = int(globalLimit/nSwitches)
swLimitAnt3LP = int(globalLimit/nSwitches)
mmpe = 0 #Média Móvel Ponderada Exponencialmente

   
def funcaoCoordenadorA(hash,total,switch,switchLimit,fim):

    global globalLimit
    global contG1A
    global contG2A
    global contG3A
    global swLimitAnt1A
    global swLimitAnt2A
    global swLimitAnt3A

    if (fim == 0):
        tabelaCoordenador[hash] = tabelaCoordenador[hash] + total   
        
        #PARA RODAR O LIMITE ADAPTATIVO DESCOMENTE ESSE BLOCO
        '''
        if (tabelaCoordenador[hash] >= globalLimit):
            if(switch==1):
                acumuladorPipe = switchA02.pegaAcumulador()
                pipesTable = switchA02.pegaResiduos()
                totalSwitch2 = somaTotalHashA(hash,acumuladorPipe,pipesTable,switch)

                acumuladorPipe = switchA03.pegaAcumulador()
                pipesTable = switchA03.pegaResiduos() 
                totalSwitch3 = somaTotalHashA(hash,acumuladorPipe,pipesTable,switch)
                print("------1------")             

                if (contG1A != 2):
                    parte1 = ((1-alfa)*swLimitAnt1A + alfa * total)
                    parte2 = ((1-alfa)*swLimitAnt2A + alfa * totalSwitch2)
                    parte3 = ((1-alfa)*swLimitAnt3A + alfa * totalSwitch3)
                    mmpe = parte1 / (parte2 + parte3)
                    limiteNovo = (mmpe * (globalLimit - (totalSwitch2 + totalSwitch3)) + total)
                    if (contG1A > 2):
                        swLimitAnt1A = switchLimit
                contG1A = contG1A + 1        
                if (contG1A == 2):
                    swLimitAnt1A = switchLimit   
                    contG1A = contG1A + 1 
               
                switchLimit = limiteNovo
                
            if(switch==2):
                acumuladorPipe = switchA01.pegaAcumulador()
                pipesTable = switchA01.pegaResiduos()
                totalSwitch1 = somaTotalHashA(hash,acumuladorPipe,pipesTable,switch)

                acumuladorPipe = switchA03.pegaAcumulador()
                pipesTable = switchA03.pegaResiduos()
                totalSwitch3 = somaTotalHashA(hash,acumuladorPipe,pipesTable,switch)   
                print("------2------") 

                if (contG2A != 2):               
                    parte1 = ((1-alfa)*swLimitAnt2A + alfa * total)
                    parte2 = ((1-alfa)*swLimitAnt1A + alfa * totalSwitch1)
                    parte3 = ((1-alfa)*swLimitAnt3A + alfa * totalSwitch3)
                    mmpe = parte1 / (parte2 + parte3)
                    limiteNovo = (mmpe * (globalLimit - (totalSwitch1 + totalSwitch3)) + total)
                    if (contG2A > 2):
                        swLimitAnt2A = switchLimit
                contG2A = contG2A + 1            
                if (contG2A == 2):
                    swLimitAnt2A = switchLimit
                    contG2A = contG2A + 1 
                      
                switchLimit = limiteNovo 
               
            if(switch==3):
                acumuladorPipe = switchA01.pegaAcumulador()
                pipesTable = switchA01.pegaResiduos()  
                totalSwitch1 = somaTotalHashA(hash,acumuladorPipe,pipesTable,switch)  

                acumuladorPipe = switchA02.pegaAcumulador()
                pipesTable = switchA02.pegaResiduos() 
                totalSwitch2 = somaTotalHashA(hash,acumuladorPipe,pipesTable,switch)
                print("------3------") 

                if (contG3A != 2):
                    parte1 = ((1-alfa)*swLimitAnt3A + alfa * total)
                    parte2 = ((1-alfa)*swLimitAnt1A + alfa * totalSwitch1)
                    parte3 = ((1-alfa)*swLimitAnt2A + alfa * totalSwitch2)
                    mmpe = parte1 / (parte2 + parte3)
                    limiteNovo = (mmpe * (globalLimit - (totalSwitch1 + totalSwitch2)) + total)
                    if (contG3A > 2):
                        swLimitAnt3A = switchLimit   
                contG3A = contG3A + 1                                     
                if (contG3A == 2):
                    swLimitAnt3A = switchLimit   
                    contG3A = contG3A + 1  
                   
                switchLimit = limiteNovo
        '''  
    if (fim == 1):
        tabelaCoordenador[hash] = tabelaCoordenador[hash] + total

    return switchLimit

def funcaoCoordenadorLP(hash,total,switch,switchLimit,fim):

    global globalLimit
    global contG1LP
    global contG2LP
    global contG3LP
    global swLimitAnt1LP
    global swLimitAnt2LP
    global swLimitAnt3LP

    if (fim == 0):
        tabelaCoordenador[hash] = tabelaCoordenador[hash] + total

        #PARA RODAR O LIMITE ADAPTATIVO DESCOMENTE ESSE BLOCO
        '''
        if (tabelaCoordenador[hash] >= globalLimit):
            if(switch==1):
                pipesTable = switchLP02.pegaResiduos()
                totalSwitch2 = somaTotalHashLP(hash,pipesTable,switch)

                pipesTable = switchLP03.pegaResiduos() 
                totalSwitch3 = somaTotalHashLP(hash,pipesTable,switch)
                print("------1------")

                if (contG1LP != 2):
                    parte1 = ((1-alfa)*swLimitAnt1LP + alfa * total)
                    parte2 = ((1-alfa)*swLimitAnt2LP + alfa * totalSwitch2)
                    parte3 = ((1-alfa)*swLimitAnt3LP + alfa * totalSwitch3)
                    mmpe = parte1 / (parte2 + parte3)
                    limiteNovo = (mmpe * (globalLimit - (totalSwitch2 + totalSwitch3)) + total)   
                    if (contG1LP > 2):
                        swLimitAnt1LP = switchLimit
                contG1LP = contG1LP + 1 
                if (contG1LP == 2):
                    swLimitAnt1LP = switchLimit 
                    contG1LP = contG1LP + 1 
                
                switchLimit = limiteNovo
                            
            if(switch==2):
                pipesTable = switchLP01.pegaResiduos()
                totalSwitch1 = somaTotalHashLP(hash,pipesTable,switch)

                pipesTable = switchLP03.pegaResiduos()
                totalSwitch3 = somaTotalHashLP(hash,pipesTable,switch)
                print("------2------")
                
                if (contG2LP != 2):
                    parte1 = ((1-alfa)*swLimitAnt2LP + alfa * total)
                    parte2 = ((1-alfa)*swLimitAnt1LP + alfa * totalSwitch1)
                    parte3 = ((1-alfa)*swLimitAnt3LP + alfa * totalSwitch3)
                    mmpe = parte1 / (parte2 + parte3)
                    limiteNovo = (mmpe * (globalLimit - (totalSwitch1 + totalSwitch3)) + total)    
                    if (contG2LP > 2):
                        swLimitAnt2LP = switchLimit   
                contG2LP = contG2LP + 1  
                if (contG2LP == 2):
                    swLimitAnt2LP = switchLimit     
                    contG2LP = contG2LP + 1   
                
                switchLimit = limiteNovo
                            
            if(switch==3):
                pipesTable = switchLP01.pegaResiduos()  
                totalSwitch1 = somaTotalHashLP(hash,pipesTable,switch)     

                pipesTable = switchLP02.pegaResiduos()          
                totalSwitch2 = somaTotalHashLP(hash,pipesTable,switch)
                print("------3------") 
                               
                if (contG3LP != 2):
                    parte1 = ((1-alfa)*swLimitAnt3LP + alfa * total)
                    parte2 = ((1-alfa)*swLimitAnt1LP + alfa * totalSwitch1)
                    parte3 = ((1-alfa)*swLimitAnt2LP + alfa * totalSwitch2)
                    mmpe = parte1 / (parte2 + parte3)
                    limiteNovo = (mmpe * (globalLimit - (totalSwitch1 + totalSwitch2)) + total)
                    if (contG3LP > 2):
                        swLimitAnt3LP = switchLimit  
                contG3LP = contG3LP + 1
                if (contG3LP == 2):
                    swLimitAnt3LP = switchLimit
                    contG3LP = contG3LP + 1
                
                switchLimit = limiteNovo
        '''       
    if (fim == 1):
        tabelaCoordenador[hash] = tabelaCoordenador[hash] + total

    return switchLimit

def somaTotalHashA(hash,acumuladorPipe,pipesTable,switch):

    i = 0
    total = 0
    residuo = 0  
    global nPipes
    
    #com pipes iguais utilizar esse bloco
    #'''
    for i in range(nPipes):
        residuo = residuo + pipesTable[i][hash]

    total = residuo + acumuladorPipe[hash]
    residuo = 0
    #'''

    #pipes diferentes utilizar esse bloco
    '''   
    if(switch==1):
        for i in range(nPipes):
            residuo = residuo + pipesTable[i][hash]

        total = residuo + acumuladorPipe[hash]
        residuo = 0
    if(switch==2):
        for i in range(nPipes):
            residuo = residuo + pipesTable[i][hash]

        total = residuo + acumuladorPipe[hash]
        residuo = 0
    if(switch==3):
        for i in range(8):
            residuo = residuo + pipesTable[i][hash]

        total = residuo + acumuladorPipe[hash]
        residuo = 0 
    '''
    return total

def somaTotalHashLP(hash,pipesTable,switch):

    residuo = 0
    i = 0
    total = 0
    global nPipes

    #pipes iguais utilizar esse bloco
    #'''
    for i in range(nPipes):
        residuo = residuo + pipesTable[i][hash]  

    total = residuo  
    residuo = 0  
    #'''

    #pipes diferentes utilizar esse bloco
    '''
    if(switch==1):
        for i in range(nPipes):
            residuo = residuo + pipesTable[i][hash]  

        total = residuo  
        residuo = 0  
    if(switch==2):
        for i in range(4):
            residuo = residuo + pipesTable[i][hash]  

        total = residuo  
        residuo = 0 
    if(switch==3):
        for i in range(8):
            residuo = residuo + pipesTable[i][hash]  

        total = residuo  
        residuo = 0     
    '''
    return total    

def controllerSwitchA(acumuladorPipe, controllerCheck, pipesTable, reports, switch,switchLimit, fim):
  
    a=0
    i = 0
    total = 0
    reachedValue = 0  
    global somaReports

    somaReports = reports + somaReports

    for a in range(len(controllerCheck)):
        hash = a
        
        #pipes iguais para os switches utilizar esse bloco
        #'''
        for i in range(nPipes):
            reachedValue = reachedValue + pipesTable[i][hash]

        total = reachedValue + acumuladorPipe[hash]
        #'''

        #pipes diferentes para os switches utilizar esse bloco
        '''
        if(switch==1):
            for i in range(nPipes):
                reachedValue = reachedValue + pipesTable[i][hash]

            total = reachedValue + acumuladorPipe[hash]
        if(switch==2):
            for i in range(nPipes):
                reachedValue = reachedValue + pipesTable[i][hash]

            total = reachedValue + acumuladorPipe[hash]
        if(switch==3):
            for i in range(8):
                reachedValue = reachedValue + pipesTable[i][hash]
        
            total = reachedValue + acumuladorPipe[hash] 
        '''
        
        funcaoCoordenadorA(hash, total, switch,switchLimit,fim)
        reachedValue = 0  
        a = a+1

def controllerSwitchLP(coordinatorVariable, nPipes, pipesTable,reports, switch,switchLimit, fim):

    reachedValue = 0
    a=0
    i = 0
    total = 0
    global somaReports

    somaReports = reports + somaReports

    for a in range(len(coordinatorVariable)):
        hash = a
        
        #pipes iguais para os switches utilizar esse bloco 
        #'''         
        for i in range(nPipes):
            reachedValue = reachedValue + pipesTable[i][hash]

        total = reachedValue
        #'''        

        #pipes diferentes paa os switches utilizar esse bloco
        '''
        if(switch==1):
            for i in range(nPipes):
                reachedValue = reachedValue + pipesTable[i][hash]

            total = reachedValue
        if(switch==2):
            for i in range(16):
                reachedValue = reachedValue + pipesTable[i][hash]

            total = reachedValue
        if(switch==3):
            for i in range(16):
                reachedValue = reachedValue + pipesTable[i][hash]

            total = reachedValue        
        '''
            
        funcaoCoordenadorLP(hash, total, switch,switchLimit,fim)
        reachedValue = 0  
        a = a+1
    
def contagem(globalLimit):

    contador = 0
    global hh

    for i in range(len(tabelaCoordenador)):
        if(tabelaCoordenador[i]>=globalLimit):
            heavyhitters[contador] = tabelaCoordenador[i]
            hh = hh+1
            contador = contador +1

def imprimir(globalLimit):
    global hh
    global somaReports

    contagem(globalLimit)

    print("/////Quantidade de HH encontrados:",hh)
    #for i in range(len(tabelaCoordenador)):
    #    if(tabelaCoordenador[i]>=globalLimit):
    #        print("--> ", i, " ", tabelaCoordenador[i], '\n') 

    print("/////Quantidade de reports ao coordenador:", somaReports)  
    print("\n")
    
def f1score():
    return tabelaCoordenador

def qHH():
    global hh
    
    return hh
