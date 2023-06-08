class Empleados:
    __DNI: str
    __nomb: str
    __dir: str
    __tel: str
    def __init__(self, dni, nombre, dir, tel):
        self.__DNI = dni
        self.__nomb = nombre
        self.__dir = dir
        self.__tel = tel
    def getDNI(self):
        return self.__DNI
    def getNombre(self):
        return self.__nomb
    def getDireccion(self):
        return self.__dir
    def getTelefono(self):
        return self.__tel

