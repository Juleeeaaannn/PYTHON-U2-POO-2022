
import os
import csv
from Viajero import Viajero
from ManejadorViajero import Lista
if __name__ == '__main__':
    band=1
    lista=Lista()
    os.system("clear")
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
                objetoV=(fila[0],fila[1],fila[2],fila[3],fila[4])
                lista.AgregarViajero(objetoV)
            continue
        
