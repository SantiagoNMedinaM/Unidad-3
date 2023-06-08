from ClaseInscripcion import Inscripcion
from ClasePersona import Persona
class Taller:
    __id: int
    __nomb: str
    __vacantes: int
    __monto: int
    __inscripciones: list
    def __init__(self,id,nomb,vacantes,monto):
        self.__id = id
        self.__nomb = nomb
        self.__vacantes = vacantes
        self.__monto = monto
        self.__inscripciones = []
    def inscribirpers(self,persona,fecha,pago):
        insr = Inscripcion(persona,fecha,pago,self)
    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nomb
    def getVacantes(self):
        return int(self.__vacantes)
    def restarVac(self):
        self.__vacantes -= 1
        return self.__vacantes
    def getMonto(self):
        return self.__monto
    def mostrarInscr(self):
        for inscripcion in self.__inscripciones:
            print(inscripcion)
    def __str__(self):
        return ("ID:{} Taller:{} Vacantes:{} Monto: {}".format(self.__id,self.__nomb,self.__vacantes,self.__monto))
    