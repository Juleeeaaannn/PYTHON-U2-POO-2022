from ClaseEmail import Email
import os
import csv
if __name__ == '__main__':
    os.system('cls')
    print('1.crear instacia de email a partir de sus atributos y modificar contraseña')
    print('2.crear objeto a partir de su direccion de correo')
    print('3.leer archivo csv, crear instancias, ingresar id para ver si esta repetido')
    inp=(int(input('ingrese a donde quiere acceder:')))
    lista=[]
    if(inp==1):
        nombre=input('Ingrese nombre de una persona:')
        idcue=input('Ingrese identificador de cuenta(ej:informatica):')
        domi=input('Ingrese dominio de cuenta(ej:gmail):')
        tipodom=input('Ingrese tipo de dominio de cuenta(ej:com):')
        print('su contraseña predeterminada es "1234".')
        ObjEmail=Email(idcue,domi,tipodom)
        print('Estimado {} te enviaremos tus mensajes a la direccion {}'.format(nombre,ObjEmail))
        password=input('ingrese contraseña actual para modificar:')
        ObjEmail.setContasena(password)
    if(inp==2):
        newobj=Email()
        nuevoEmail=input('ingrese email para crear un objeto:')
        nuevoEmail=newobj.crearCuenta(nuevoEmail)
    if(inp==3):
        archivo= open('correos.csv')
        cont=0
        reader=csv.reader(archivo,delimiter=',')
        ide=input('ingrese identificador a buscar: ')
        for fila in reader:
            print(fila[0])
            if (fila[0] == ide):
                cont += 1
        print('la cantidad de personas que tienen el mismo identificador {} son {}'.format(ide,cont))
        if(cont>1):
            print('el identificador se repite')
        elif(cont<1):
            print('el identificador no se repite')
        archivo.close()
