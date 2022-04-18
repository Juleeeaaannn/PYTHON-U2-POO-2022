from pickle import NONE


class Email:
    __idCuenta=''
    __dominio=''
    __tipoDominio=''
    __contrasena=''
    def __init__ (self,idCuenta='',domini='',tipoDominio='',contra='1234'):
        self.__idCuenta=idCuenta
        self.__dominio=domini
        self.__tipoDominio=tipoDominio
        self.__contrasena=contra
    def __str__(self):
        return('{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDominio))
    def getDominio(self):
        return self.__dominio
    def crearCuenta(self,cuenta):
        if ((cuenta.find("@") != -1) & (cuenta.find(".") != -1)):
            nuevoemail=self.__init__(cuenta[:cuenta.find('@')], cuenta[cuenta.find('@')+1:cuenta.find('.')],cuenta[cuenta.find('.')+1:], contra=input('ingrese la contraseña para el nuevo objeto:'))
            print('nuevo objeto creado')
            return nuevoemail
        else: print('error correo.')
    def setContasena(self,contra):
        if(self.__contrasena==contra):
            nueva=input('ingrese nueva contraseña: ')
            self.__contrasena=nueva
            print('su nueva contraseña es: {}'.format(self.__contrasena))
        else: print('las contraseñas no coinciden')
