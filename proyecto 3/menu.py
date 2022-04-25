class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher= {'1':self.opcion1,
                          '2':self.opcion2,
                          '3':self.opcion3,
                          '4':self.salir}
    def opcion(self,op,manejador):
        func= self.__switcher.get(op,lambda: print('Opcion no valida'))
        if(op=='1' or op=='2' or op=='3'):
            func(manejador)
        else:
            func()
    def salir(self):
        print('terminado!')