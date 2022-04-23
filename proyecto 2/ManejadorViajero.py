from viajero import Viajero
class Lista:
    __viajeros=[]
    def __init__(self):
        self.__viajeros=[]
    def AgregarViajero(self,objetoViajero):
        self.__viajeros.append(objetoViajero)
    def GetViajero(self,numViajero):
        for indice,viaje in enumerate(self.__viajeros):
            if( viaje.getNumViajero() == numViajero):
                return indice
    def GetMillas(self,indice):
        return self.__viajeros[indice].cantidadTotaldeMillas()
    def SetAcumMillas(self,indice,acum):
        valor=self.__viajeros[indice].acumularMillas(acum)
        return valor
    def CanjeMillas(self,indice,acum):
        return self.__viajeros[indice].canjearMillas(acum)
