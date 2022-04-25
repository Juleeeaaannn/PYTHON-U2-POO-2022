from numpy import append
from registro import Registro
import csv

class ManejadorRegistro:
    __dia = 30
    __hora = 24
    __lista=[]
    def __init__(self):
        for i in range(self.__dia):
            self.__lista.append([])
            for j in range(self.__hora):
                self.__lista[i].append(0)
    def Agregar(self, elemento):
        for i in range(self.__dia):
            for j in range(self.__hora):
                self.__lista[i].append(elemento)
    def LeerArchivo(self):
        bandera=True
        archivo=open('registro.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            if(bandera):
                bandera=False
            else:
                d=int(fila[0])
                h=int(fila[1])
                t=float(fila[2])
                h=int(fila[3])
                p=int(fila[4])
                reg=Registro(t,h,p)
                self.__lista[d-1][h-1]=reg
                print('leido')
    def MostrarRegistroMayoryMenor(self):
        mayort=0
        mayorh=0
        mayorp=0
        menort=9999999
        menorh=9999999
        menorp=9999999
        for i in range(self.__dia):
            for j in range(self.__hora):
                if(self.__lista[i][j].getTemperatura>mayort):
                    mayort=self.__lista[i][j].getTemperatura
                if(self.__lista[i][j].getHumedad>mayorh):
                    mayorh=self.__lista[i][j].getHumedad
                if(self.__lista[i][j].getPresion>mayorp):
                    mayorp=self.__lista[i][j].getPresion

                if(self.__lista[i][j].getTemperatura<menort):
                    menort=self.__lista[i][j].getTemperatura
                if(self.__lista[i][j].getHumedad<menorh):
                    menorh=self.__lista[i][j].getHumedad
                if(self.__lista[i][j].getPresion<menorp):
                    menorp=self.__lista[i][j].getPresion
        print('Mayor temperatura:{} Menor Temperatura:{}'.format(mayort,menort))
        print('Mayor humedad:{} Menor humedad:{}'.format(mayorh,menorh))
        print('Mayor presion:{} menor presion{}'.format(mayorp,menorp))


