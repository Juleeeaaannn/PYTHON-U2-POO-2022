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
                pt=float(fila[6])
                objeto=Medicamentos(ic,im,nc,mo,pr,ca,pt)
                self.__lista.append(objeto)
        print('archivo Medicamentos leido')
    def Mostrar(self,ide):
        acum=0.0
        for a in self.__lista:
            if a.getId() == ide:
                print('{}'.format(a.getMonodroga()),end='\t\t')
                print('{}'.format(a.getPresentacion()),end='\t\t')
                print('{}'.format(a.getCantidad()),end='\t\t')
                print('{}'.format(a.getPrecio()))
                acum=acum+a.getPrecio()
        print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
        print('total adeudado:','{}'.format(acum),sep='\t\t\t\t\t\t\t')