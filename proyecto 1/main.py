import os
import csv
from ClaseEmail import Email
if __name__ == '__main__':
    band=1
    os.system('cls')
    while(band!=-1):
        print('1.crear instacia de email a partir de sus atributos y modificar contraseña')
        print('2.crear objeto a partir de su direccion de correo')
        print('3.leer archivo csv, crear instancias, ingresar id para ver si esta repetido')
        print('4.borrar pantalla')
        print('5.terminar')
        inp=input('ingrese a donde quiere acceder:')
        if(inp=='1'):
            nombre=input('Ingrese nombre de una persona:')
            idcue=input('Ingrese identificador de cuenta(ej:informatica):')
            domi=input('Ingrese dominio de cuenta(ej:gmail):')
            tipodom=input('Ingrese tipo de dominio de cuenta(ej:com):')
            print('su contraseña predeterminada es "1234".')
            ObjEmail=Email(idcue,domi,tipodom)
            print('Estimado {} te enviaremos tus mensajes a la direccion {}'.format(nombre,ObjEmail))
            ObjEmail.setContasena()
            continue
        if(inp=='2'):
            newobj=Email()
            nuevoEmail=input('ingrese email para crear un objeto:')
            nuevoEmail=newobj.crearCuenta(nuevoEmail)
            continue
        if(inp=='3'):
            archivo= open('correos.csv')
            cont=0
            reader=csv.reader(archivo,delimiter=',')
            ide=input('ingrese identificador a buscar: ')
            for fila in reader:
                if (fila[0] == ide):
                    cont += 1
                objetocsv=Email(fila[0],fila[1],[fila[2],fila[3]])
            print('la cantidad de personas que tienen el mismo identificador {} son {}'.format(ide,cont))
            if(cont>1):
                print('el identificador se repite')
            elif(cont<1):
                print('el identificador no se repite')
            archivo.close()
            continue
        if(inp=='4'):
            os.system('cls')
        if(inp=='5'):
            band=-1
