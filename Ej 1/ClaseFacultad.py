from ClaseCarrera import Carrera
class  Facultad:
    __cod = int
    __nomb = str
    __direc = str
    __localidad = str
    __tel = str
    __carreras = list
    def __init__(self, cod, nomb, direc, loc, tel):
        self.__cod = cod
        self.__nomb = nomb
        self.__direc = direc
        self.__localidad = loc
        self.__tel = tel
        self.__carreras = []
    def addCarrera(self,carrera):
        self.__carreras.append(carrera)
    def __str__(self):
        return "{:<15}{:<25}{:<40}{:<30}".format(self.__cod,self.__nomb,self.__direc,self.__localidad)
    def mostrar(self):
        print("{:<15}{:<25}{:<40}{:<30}".format("Codigo","Nombre","Direccion","Localidad","Telefono"))
        print(self)
        print("Carreras")
        print("{:<15}{:<25}{:<10}{:<10}{:<10}".format("Codigo","Carrera","Fecha","Duracion","Titulo"))
        for i in range(len(self.__carreras)):
            print(self.__carreras[i])
    def getCod(self):
        return self.__cod
    def getNombre(self):
        return self.__nomb
    def getDirec(self):
        return self.__direc
    def getLocalidad(self):
        return self.__localidad
    def getTelefono(self):
        return self.__tel
    def getCarreras(self):
        return self.__carreras
    def buscarCarr(self,carrera):
        i = 0
        c = None
        band = False
        while i < len(self.__carreras) and not band:
            if (carrera == self.__carreras[i].getNombre()):
                print("d")
                c = i
                band = True
            i+=1
        return c
    def mostrarfacu(self, pos):
        for i in range(len(self.__carreras)):
            if (i==pos):
                print("f")
                print ("Codigo:{}.{}, Nombre:{}, Localidad:{}".format(self.__cod,self.__carreras[i].getCod(),self.__nomb,self.__localidad))