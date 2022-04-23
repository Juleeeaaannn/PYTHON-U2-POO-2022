import os
import csv
from pickle import NONE
from viajero import Viajero
from ManejadorViajero import Lista
if __name__ == '__main__':
    band=1
    lista=Lista()
    os.system("cls")
    while(band!=-1):
        print('1.leer un archivo,crear instancias de la clase y almacenarlas en una lista')
        print('2.ingrese un número de viajero frecuente ')
        print('3.borrar pantalla')
        print('4.terminar')
        inp=input('ingrese a donde quiere acceder:')
        if(inp=='1'):
            archivo=open("viajero.csv")
            reader=csv.reader(archivo,delimiter=';')
            for fila in reader:
                objetoV=Viajero(fila[0],fila[1],fila[2],fila[3],fila[4])
                lista.AgregarViajero(objetoV)
            print('Archivo Leido Correctamente!\n')
            continue
        elif(inp=='2'):
            os.system("cls")
            numViajero =input('ingrese un número de viajero frecuente: ')
            indice = lista.GetViajero(numViajero)
            if(indice==None):
                print('\nEl numero de viajero es incorrecto\n')
            print('\n1.Consultar Cantidad de Millas')
            print('2.Acumular Millas')
            print('3.Canjear Millas')
            op=input('ingrese a donde quiere acceder: ')
            if(op=='1'):
                millas=lista.GetMillas(indice)
                print('\nla cantidad total de millas es: {}\n'.format(millas))
                continue
            elif(op=='2'):
                acum=int(input('\nIngrese cantidad de millas recorridas: \n'))
                valor=lista.SetAcumMillas(indice,acum)
                print('\nEl valor actualizado de sus millas son: {}\n'.format(valor))
                continue
            elif(op=='3'):
                canje=int(input('\nIngrese cantidad de millas a canjear: '))
                millacanje=lista.CanjeMillas(indice,canje)
                if(millacanje!=None):
                    print('\n cantidad de millas actuales: {}'.format(millacanje))
        elif(inp=='3'):
            os.system("cls")
        elif(inp=='4'):
            band=-1
            