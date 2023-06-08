from ClaseInscripcion import Inscripcion
class  Persona:
    __nombre: str
    __direc: str
    __dni: str
    def __init__(self, nomb, direc, dni):
        self.__nombre = nomb
        self.__direc = direc
        self.__dni = dni
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direc
    def getDni(self):
        return self.__dni
    def __str__(self) -> str:
         return ("{:<15}{:<30}{:<15}".format(self.__nombre,self.__direc,self.__dni))