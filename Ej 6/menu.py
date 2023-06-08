from ClaseNuevo import Nuevo
from ClaseObjectEncoder import ObjectEncoder
from ClaseUsado import Usado
class Menu:
    __opcion : int
    
    def __init__(self):
        self.__opcion = 0

    def opciones(self,vehiculos):
        vehiculos.mostrarLista()
        while self.__opcion != 8:
            print("Menu de Opciones")
            print("1)- Insertar un vehiculo en una posicion determinada")
            print("2)- Agregar un vehiculo a la coleccion")
            print("3)- Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
            print("4)- Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
            print("5)- Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.")
            print("6)- Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
            print("7)- Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.")
            print("8)- SALIR")
            self.__opcion = int(input("\nIngrese una opcion: "))

            if self.__opcion == 1:
                tipo = str(input("Que vehiculo desea ingresar 'U': usado, 'N': nuevo: "))
                marca = str(input("Ingrese la marca: "))
                modelo = str(input("Ingrese el modelo: "))
                puertas = int(input("Ingrese la cantidad de puertas: "))
                color = str(input("Ingrese el color: "))
                precio = int(input("Ingrese el precio base: "))
                if tipo == 'U' or tipo == 'u':
                    patente = str(input("Ingrese la patente: "))
                    anio = int(input("Ingrese el anio: "))
                    kms = int(input("Ingrese el kilometraje: "))
                    vehiculo = Usado(modelo,puertas,color,precio,marca,patente,anio,kms)

                elif tipo == 'N' or tipo == 'n':

                    version = str(input("Ingrese la version del vehiculo (base o full):"))
                    vehiculo = Nuevo(modelo,puertas,color,precio,marca,version)

                posicion = int(input("Ingrese una posicion de la lista para insertar el vehiculo: "))
                vehiculos.insertarElemento(vehiculo, posicion)

            elif self.__opcion == 2:
                tipo = str(input("Que vehiculo desea ingresar 'U': usado, 'N': nuevo: "))
                
                marca = str(input("Ingrese la marca: "))
                modelo = str(input("Ingrese el modelo: "))
                puertas = int(input("Ingrese la cantidad de puertas: "))
                color = str(input("Ingrese el color: "))
                precio = int(input("Ingrese el precio base: "))
                if tipo == 'U' or tipo == 'u':
                    patente = str(input("Ingrese la patente: "))
                    anio = int(input("Ingrese el anio: "))
                    kms = int(input("Ingrese el kilometraje: "))
                    vehiculo = Usado(modelo,puertas,color,precio,marca,patente,anio,kms)

                elif tipo == 'N' or tipo == 'n':

                    version = str(input("Ingrese la version del vehiculo (base o full):"))
                    vehiculo = Nuevo(modelo,puertas,color,precio,marca,version)

                vehiculos.agregarV(vehiculo)

            elif self.__opcion == 3:
                posicion = int(input("Ingrese una posicion de la lista para mostrar el tipo de vehiculo: "))
                vehiculos.mostrarElemento(posicion)

            elif self.__opcion == 4:
                ingpat = str(input("Ingrese una patente de un vehiculo usado: "))
                band = vehiculos.existePatente(ingpat)
                if band == False:
                    print("La patente ingresada no existe")
                else:
                    nuevoprecio = float(input("Ingrese el nuevo precio base del vehiculo: "))
                    vehiculos.modificaPrecio(ingpat, nuevoprecio)
                    vehiculos.mostrarValor(ingpat)

            elif self.__opcion == 5:
                print("Vehiculo mas economico: ")
                vehiculos.masEconomico()

            elif self.__opcion == 6:
                print("{:<20}{:<20}{:<20}".format("Modelo","Cantidad de puertas","Importe de venta"))
                vehiculos.vehiculosConcesionaria()

            elif self.__opcion == 7:
                jsonF = ObjectEncoder()
                d = vehiculos.toJSON()
                jsonF.guardar(d,"vehiculos (2).json")

            elif self.__opcion == 8:
                print("FIN DEL PROGRAMA")

            else:
                print("Opcion incorrecta, ingrese otra opcion ")
