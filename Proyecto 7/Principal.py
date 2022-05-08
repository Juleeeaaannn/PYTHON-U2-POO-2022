from viajero import Viajero
if __name__=='__main__':
    viajero1=Viajero('1','12345','julian','molina',1000)
    viajero2=Viajero('2','123456','joaquin','luna',2000)
    print('--------------Valores iniciales---------------')
    print('viajero 1:',viajero1,'viajero 2:',viajero2)
    print('----------------sobrecarga -----------------')
    print('--------------viajero1<viajero2---------------')
    if(viajero1<viajero2):
        print('las millas de viajero 2 es mayor al viajero 1')
    else:
        print('las millas del viajero 1 es mayor al viajero 2')
    print('----------------sobrecarga ADD----------------')
    print('------------Viajero1=Viajero1+100-------------')
    print('------------Viajero2=Viajero2+100-------------')
    viajero1=viajero1+100
    viajero2=viajero2+100
    print('viajero1:',viajero1)
    print('viajero2:',viajero2)
    print('----------------sobrecarga SUB----------------')
    print('------------Viajero1=Viajero1-100-------------')
    print('------------Viajero2=Viajero2-100-------------')
    viajero1=viajero1-100
    viajero2=viajero2-100
    print('viajero1:',viajero1)
    print('viajero2:',viajero2)
    print('----------------sobrecarga EQ----------------')
    print('----------------100==viajero1----------------')
    print('----------------viajero2==100----------------')
    if(100==viajero1):
        print('las millas de viajero 1 es igual a 100')
    else:
        print('las millas de viajero 1 NO es igual a 100')
    if(viajero2==100):
        print('las millas de viajero 2 es igual a 100')
    else:
        print('las millas de viajero 2 NO es igual a 100')
    print('----------------sobrecarga RADD----------------')
    print('--------------viajero=viajero+100--------------')
    print('--------------viajero=100+viajero--------------')
    viajero1=viajero1+100
    viajero2=100+viajero2
    print(viajero1)
    print(viajero2)
    print('----------------sobrecarga RSUB----------------')
    print('--------------viajero=viajero-100--------------')
    print('--------------viajero=100-viajero--------------')
    viajero1=viajero1-100
    v=100-viajero2
    print(viajero1)
    print(viajero2)


    

