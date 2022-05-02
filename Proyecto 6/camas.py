from tkinter import N


class Camas:
    __idCama=None
    __habitacion=None
    __estado=None
    __apellidoNombre=None
    __diagnostico=None
    __observacion=None
    __fechaInternacion=None
    __fechaAlta=None
    def __init__(self,idcama=1,habitacion='',estado=None,apellidoNombre='',diagnostico='',observacion='',fechaInternacion='',fechaAlta=''):
        self.__idCama=idcama
        self.__habitacion=habitacion
        self.__estado=estado
        self.__apellidoNombre=apellidoNombre
        self.__diagnostico=diagnostico
        self.__fechaInternacion=fechaInternacion
        self.__fechaAlta=fechaAlta
        self.__observacion=observacion
    def getAyN(self):
        return self.__apellidoNombre
    def getId(self):
        return self.__idCama
    def getHabitacion(self):
        return self.__habitacion
    def getDiagnostico(self):
        return self.__diagnostico
    def getFechaI(self):
        return self.__fechaInternacion
    def getFechaAlta(self):
        return self.__fechaAlta
    def setEstado(self,estadonew):
        self.__estado=estadonew
        