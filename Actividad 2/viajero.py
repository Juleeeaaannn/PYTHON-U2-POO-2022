class Viajero:
    __num_viajero=0
    __dni=0
    __nombre=''
    __apellido=''
    __millas_acum=''
    def __init__(self,num_viajero,dni,nombre,apellido,millas_acum):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum
    def cantidadTotaldeMillas(self):
        pass
    def acumularMillas(self):
        pass
    def canjearMillas(self):
        pass