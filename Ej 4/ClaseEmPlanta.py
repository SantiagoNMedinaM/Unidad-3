from ClaseEmpleados import Empleados
class DePlanta(Empleados):
    __sueldoBasico: float
    __antiguedad: int
    def __init__(self, dni, nombre, dir, tel, sueldob, anti):
        super().__init__(dni, nombre, dir, tel)
        self.__sueldoBasico = sueldob
        self.__antiguedad = anti
    def getSueldoBasico(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    def getSueldo(self):
        sueldo = float(self.__sueldoBasico) + (float(self.__sueldoBasico)*0.01)*float(self.__antiguedad)
        return sueldo