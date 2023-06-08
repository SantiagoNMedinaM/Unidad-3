from ClaseEmpleados import Empleados
import datetime
class Contratado(Empleados):
    __fechaIn: datetime
    __fechaFin: datetime
    __cantHs: int
    __pph: float
    def __init__(self, dni, nombre, dir, tel,fechaIn,fechaFin,cantHs,pph):
        super().__init__(dni, nombre, dir, tel)
        self.__fechaFin = fechaIn
        self.__fechaFin = fechaFin
        self.__cantHs = cantHs
        self.__pph = pph
    def getFechaIn(self):
        return self.__fechaIn
    def getFechaFin(self):
        return self.__fechaFin
    def getCantHs(self):
        return self.__cantHs
    def getValorPH(self):
        return self.__pph
    def getSueldo(self):
        sueldo = float(self.__cantHs)*float(self.__pph)
        return sueldo
    def modificarHoras(self,hs):
        self.__cantHs += int(hs)