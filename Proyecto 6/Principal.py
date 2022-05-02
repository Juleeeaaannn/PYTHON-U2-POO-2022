from manejadorC import ManejadorCamas
from manejadorM import ManejadorMedicamentos
if __name__=='__main__':
    listaM=ManejadorMedicamentos()
    listaC=ManejadorCamas()
    listaM.LeerArchivo()
    listaC.LeerArchivo()
    print('````````````````````````````````````````````````````````````````````````````````````')
    paciente=input('Ingrese Apellido y Nombre del paciente a buscar (con una coma entre medio):')
    listaC.Buscar(listaM,paciente)
