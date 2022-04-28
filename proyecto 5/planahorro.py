from mimetypes import init


class PlanAhorro:
    __codigo=0
    __modelo=''
    __version=0
    __valor=0.0
    cantiCuotas=0
    cantiPagas=0
    def __init__(self,codigo,modelo,version,valor):
        self.__codigo=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
    