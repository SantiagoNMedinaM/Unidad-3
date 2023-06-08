from claseEmpleado import Empleado
class Menu:
    __opcion=0

    def __init__(self):
        self.__opcion=0

    def opciones(self,m):
        while self.__opcion!=4:
            print('1--Ingresar elemento por posicion\n2--Ingresar elemento al final\n3--Mostrar elemento por posicion\n')
            self.__opcion=int(input('Ingrese una opcion '))
            if self.__opcion == 1:
                dni = int(input("Ingrese el DNI de la persona: "))
                nomb = str(input("Ingrese el nombre de la persona: "))
                dir = str(input("Ingrese la direccion de la persona: "))
                tel = int(input("Ingrese el telefono de la persona: "))
                inst = Empleado(dni,nomb,dir,tel)
                ind = int(input("Ingrese la posicion donde desea agregar a la persona"))
                m.insertarElem(inst,ind)
            if self.__opcion == 2:
                dni=int(input('Ingrese dni de la persona '))
                nombre=str(input('Ingrese nombre de la persona '))
                direccion=str(input('Ingrese direccion de la persona '))
                telefono=str(input('Ingrese telefono de la persona '))
                unempleado=Empleado(dni,nombre,direccion,telefono)
                m.agregarElemento(unempleado)
            elif self.__opcion==3:
                posicion=int(input('Ingrese posicion del elemento a mostrar '))
                m.mostrarElemento(posicion)
            elif self.__opcion==4:
                print('SALIENDO DEL PROGRAMA')  
            else:
                print('Opcion ingresada incorrecta ')