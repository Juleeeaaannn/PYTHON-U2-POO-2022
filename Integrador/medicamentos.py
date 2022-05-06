class Medicamentos:
    __idCama=None
    __idMedicamento=None
    __nombreComercial=None
    __monodroga=None
    __presentacion=None
    __cantidadAplicada=None
    __precioTotal=None
    def __init__(self,idcama=1,idMedicamento=1,nombreComercial='',monodroga='',presentacion='',cantidadAplicada='',precioTotal=0.0):
        self.__idCama=idcama
        self.__idMedicamento=idMedicamento
        self.__nombreComercial=nombreComercial
        self.__monodroga=monodroga
        self.__presentacion=presentacion
        self.__cantidadAplicada=cantidadAplicada
        self.__precioTotal=precioTotal
    def getId(self):
        return self.__idCama
    def getMonodroga(self):
        return self.__monodroga
    def getPresentacion(self):
        return self.__presentacion
    def getCantidad(self):
        return self.__cantidadAplicada
    def getPrecio(self):
        return self.__precioTotal