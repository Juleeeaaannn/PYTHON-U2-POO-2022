import csv
class Manejador:
    lista=[]
    def __init__(self):
        self.__lista=[]
    def Agregar(self,elemento):
        self.__lista.append(elemento)
    def inicio(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            c=fila[0]
            m=fila[1]
            ve=fila[2]
            va=fila[3]
            