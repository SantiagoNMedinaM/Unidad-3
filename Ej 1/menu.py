class MenuOpciones:
    __opcion = int
    def __init__(self):
        self.__opcion = 0
    def opciones (self,lf):
        while self.__opcion != 3:
            print("1: Mostrar nombre de la facultad, nombre  y duración de cada carrera.\n2: Dado el nombre de una carrera, mostrar código, nombre y localidad de la facultad.")
            self.__opcion = int(input("Ingrese la opcion deseada: "))
            if self.__opcion == 1:
                cod = int(input("Ingrese codigo de la facultad deseada: "))
                lf.muestrafac(cod)
            elif self.__opcion == 2:
                carr = str(input("Ingrese la carrera a buscar: "))
                lf.muestracarr(carr)
             