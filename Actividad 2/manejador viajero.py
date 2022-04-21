from Viajero import Viajero
class Lista:
    __viajeros=[]
    def __init__(self):
        self.__viajeros=[]
    def AgregarViajero(self,objetoViajero):
        self.__viajeros.append(objetoViajero)
    def MostrarViajeros(self):
        for viajeros in self.__viajeros:
            viajeros.MostrarViajero
