class Viajero:
    __num_viajero=0
    __dni=0
    __nombre=''
    __apellido=''
    __millas_acum=int
    def __init__(self,num_viajero=0 ,dni=0,nombre='',apellido='',millas_acum=0):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=int(millas_acum)
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    def acumularMillas(self,milla):
        print(type(self.__millas_acum))
        self.__millas_acum+=milla
        return self.__millas_acum
    def canjearMillas(self,canti):
        if(canti <= self.__millas_acum):
            self.__millas_acum=self.__millas_acum-canti
            return self.__millas_acum
        else:print('error al canjear millas!')

        pass
    def getNumViajero(self):
        return self.__num_viajero
    def __str__(self):
        return('NUM:{} nombre:{} apellido:{} dni:{} millasacum:{}'.format(self.__num_viajero,self.__nombre,self.__apellido,self.__dni,self.__millas_acum))