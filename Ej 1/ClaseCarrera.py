class Carrera:
    __cod = int
    __nomb = str
    __fechain = str
    __duracion = str
    __titulo = str
    def __init__(self, cod, nomb, fecha, duracion, titulo):
        self.__cod = cod
        self.__nomb = nomb
        self.__fechain = fecha
        self.__duracion = duracion
        self.__titulo = titulo
    def __str__(self):
        return "{:<15}{:<25}{:<10}{:<10}{:<10}".format(self.__cod,self.__nomb,self.__fechain,self.__duracion,self.__titulo)
        #return self.__cod+ " " +self.__nomb+ " " +self.__fechain+ " " +self.__duracion+ " " +self.__titulo
    def getCod(self):
        return self.__cod
    def getNombre(self):
        return self.__nomb
    def getFechain(self):
        return self.__fechain
    def getDuracion(self):
        return self.__duracion
    def getTitulo(self):
        return self.__titulo