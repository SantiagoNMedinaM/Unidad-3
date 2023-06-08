from ManejadorEmpleados import ManeEmpleados
import datetime
class Menu:
    __opcion: int
    def __init__(self):
        self.__opcion = 0
    def opciones(self,le):
         while self.__opcion != 5:
            print("---MENU DE OPCIONES---")
            print("1)- Registrar horas.")
            print("2)- Total de tarea")
            print("3)- Ayuda economica")
            print("4)- Calcular sueldo")
            print("5)- Salir")
            self.__opcion = int(input("Ingrese una opcion "))
            if self.__opcion == 1:
                dni = str(input("Ingrese DNI del empleado a registrar horas: "))
                pos = le.buscarDni(dni)
                if pos != None:
                    hs = int(input("Ingrese horas a registrar: "))
                    le.registrar(pos,hs)
            elif self.__opcion == 2:
                tarea = str(input("Ingrese la tarea deseada: "))
                fecha = datetime.datetime.now()
                le.totalTarea(tarea,fecha)
            elif self.__opcion == 3:
                le.ayudaEco()
            elif self.__opcion == 4:
                le.showAll()
 