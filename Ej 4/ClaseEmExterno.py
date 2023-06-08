import datetime
from ClaseEmpleados import Empleados
class Externo(Empleados):
    __tareaEsp: str
    __fechaIn: datetime
    __fechaFin: datetime
    __monViat: float
    __manoDeO: float
    __montSdV: float
    def __init__(self, dni, nombre, dir, tel,tarea,fechain,fechafin,manViat,mano,mont):
        super().__init__(dni, nombre, dir, tel)
        self.__tareaEsp = tarea
        self.__fechaIn = fechain
        self.__fechaFin = fechafin
        self.__monViat = manViat
        self.__manoDeO = mano
        self.__montSdV = mont
        
    def getTarea(self):
        return self.__tareaEsp
    def getFechain(self):
        return self.__fechaIn
    def getFechaFin(self):
        return self.__fechaFin
    def getMontoViatico(self):
        return self.__monViat
    def getManoDeObra(self):
        return self.__manoDeO
    def getMontoSdV(self):
        return self.__montSdV
    def getSueldo(self):
        sueldo = float(self.__manoDeO) - float(self.__monViat) - float(self.__montSdV)
        return sueldo
