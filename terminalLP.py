#------------ TERMINAL LOCAL-PIPE --------------

import switchLP01
import switchLP02
import switchLP03
#import switchLP04
#import switchLP05
#import switchLP06
import threading
import coordenador
import valores
import f1Score

nSwitches = valores.qntDeSwitches()
globalLimit = valores.limiteGlobal()
nPipes = valores.qntDePipes()
alfa = valores.alfa()
switchLimit = int(globalLimit/nSwitches)
import resource
import os


def executar():

    def s1():
        switchLP01.main()

    def s2():
        switchLP02.main()

    def s3():
        switchLP03.main()
    
    #def s4():
    #    switchLP04.main()

    #def s5():
    #    switchLP05.main()

    #def s6():
    #    switchLP06.main()

    t1 = threading.Thread(target=s1)
    t2 = threading.Thread(target=s2)
    t3 = threading.Thread(target=s3)
    #t4 = threading.Thread(target=s4)
    #t5 = threading.Thread(target=s5)
    #t6 = threading.Thread(target=s6)

    t1.start()
    t2.start()
    t3.start()
    #t4.start()
    #t5.start()
    #t6.start()

    t1.join()
    t2.join()
    t3.join()
    #t4.join()
    #t5.join()
    #t6.join()

def main():

    global globalLimit
    print("\n  --- LOCAL PIPE ---\n")
    print("Limite Global:", globalLimit)
    print("Quantidade de Switches:", nSwitches)
    print("Quantidade de pipes:", nPipes)
    print("Alfa:", alfa)
    print("\ntrafego iniciado...\n")

    executar()
    coordenador.imprimir(globalLimit)
    f1Score.main()

if __name__ == '__main__':
    main()
