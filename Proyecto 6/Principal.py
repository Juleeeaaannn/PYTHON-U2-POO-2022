from viajero import Viajero
if __name__=='__main__':
    viajero1=Viajero('1','12345','julian','molina',100)
    viajero2=Viajero('2','123456','joaquin','luna',200)
    print('--------------Valores iniciales---------------')
    print('viajero 1:',viajero1,'viajero 2:',viajero2)
    print('----------------sobrecarga GT-----------------')
    print('--------------viajero1<viajero2---------------')
    if(viajero1>viajero2):
        print('el viajero 1 tiene mas millas acumuladas')
    else:
        print('el viajero 2 tiene mas millas acumuladas')
    print('----------------sobrecarga ADD----------------')
    print('------------Viajero1=Viajero1+100-------------')
    print('------------Viajero2=Viajero2+100-------------')
    viajero1=viajero1+100
    viajero2=viajero2+100
    print(viajero1)
    print(viajero2)
    print('----------------sobrecarga SUB----------------')
    print('------------Viajero1=Viajero1-100-------------')
    print('------------Viajero2=Viajero2-100-------------')
    viajero1=viajero1-100
    viajero2=viajero2-100
    print(viajero1)
    print(viajero2)
