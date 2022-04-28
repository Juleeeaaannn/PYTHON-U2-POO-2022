class Ventana:
    __titulo=''
    __xizq=0
    __yizq=0
    __xder=0
    __yder=0
    def __init__(self,titulo='',xizq=0,yizq=0,xder=0,yder=0):
        self.__titulo=titulo
        self.__xizq=xizq
        self.__yizq=yizq
        self.__xder=xder
        self.__yder=yder
    def mostrar(self):
        print('titulo:{}'.format(self.__titulo))
        print('X superior izquierdo:{}   Y superior izquierdo:{}'.format(self.__xizq,self.__yizq))
        print('X inferior derecho:{}    Y inferior derecho:{}'.format(self.__xder,self.__yder))
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return self.__yder-self.__yizq
    def ancho(self):
        return self.__xder-self.__xizq
    def moverDerecha(self,num=1):
        self.__xder+=num
        self.__xizq+=num
    def moverIzquierda(self,num=1):
        self.__xizq-=num
        self.__xder-=num
    def subir(self,num=1):
        self.__yizq+=num
        self.__yder+=num
    def bajar(self,num=1):
        self.__yizq-=num
        self.__yder-=num