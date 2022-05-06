import csv
import numpy as np
from camas import Camas
from manejadorM import ManejadorMedicamentos as MM
class ManejadorCamas:
    __dimesion=30
    __cantidad=0
    def __init__(self):
        self.__camas=np.empty(self.__dimesion,dtype=Camas) #dimension es la cantidad de elementos en el arreglo y type es el tipo de elementos que se van a agregar
        self.__cantidad=0
    def agregarCama(self,cama):
        self.__camas[self.__cantidad]=cama #AGREGO UNA CAMA AL ARREGLO
        self.__cantidad+=1 #ACUMULO CANTIDAD DE CAMAS 
    def LeerArchivo(self):
        band=True
        archivo=open('camas.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if(band):
                band=False
            else:
                id=fila[0]
                ha=fila[1]
                es=bool(fila[2])
                ap=fila[3]
                di=fila[4]
                ob=fila[5]
                fi=fila[6]
                fa=fila[7]
                objeto=Camas(id,ha,es,ap,di,ob,fi,fa)
                self.agregarCama(objeto)
        print('archivo camas leido')
    def Buscar(self,listaM,elemento):
        i=0
        if type ((listaM) == MM):
            while(i<self.__cantidad and self.__camas[i].getAyN()!=elemento):
                i+=1
            if(i<self.__cantidad):
                print('````````````````````````````````paciente encontrado!````````````````````````````````')
                print('Paciente:{}'.format(self.__camas[i].getAyN()),end='\t')
                print('Cama:{}'.format(self.__camas[i].getId()),end='\t')
                print('Habitacion:{}'.format(self.__camas[i].getHabitacion()))
                
                print('diagnostico:{}'.format(self.__camas[i].getDiagnostico()),end='\t')
                print('Fecha de internacion:{}'.format(self.__camas[i].getFechaI()))

                print('fecha de alta:{}'.format(self.__camas[i].getFechaAlta()))
                
                print('Medicamento/Monodroga',end='\t')
                print('Presentacion',end='\t\t')
                print('Cantidad',end='\t')
                print('Precio')
                listaM.Mostrar(self.__camas[i].getId())
            else: print('paciente no encontrado!')