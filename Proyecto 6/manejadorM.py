import csv
from medicamentos import Medicamentos
class ManejadorMedicamentos:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def LeerArchivo(self):
        band=True
        archivo=open('medicamentos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if(band):
                band=False
            else:
                ic=fila[0]
                im=fila[1]
                nc=fila[2]
                mo=fila[3]
                pr=fila[4]
                ca=fila[5]
                pt=fila[6]
                objeto=Medicamentos(ic,im,nc,mo,pr,ca,pt)
                self.__lista.append(objeto)
        print('archivo Medicamentos leido')
