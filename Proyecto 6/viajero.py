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
    def getMillas(self):
        return self.__millas_acum
    def __gt__(self,otro):
        if(self.__millas_acum > otro.getMillas()):
            resultado=self.__millas_acum
        else:
            resultado=False
        return resultado
    def __add__(self,otro):
        return (self.__millas_acum+otro)
    def __sub__(self,otro):
        return (self.__millas_acum-otro)
    def __str__(self):
        return ('{}'.format(self.__millas_acum))