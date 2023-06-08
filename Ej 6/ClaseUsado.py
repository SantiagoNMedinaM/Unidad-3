from ClaseVehiculo import Vehiculo
import datetime
class Usado(Vehiculo):
    __patente: str
    __anio: int
    __kms: int
    def __init__(self, modelo, cantP, color, precioBase, marca,patente,anio, kms):
        super().__init__(modelo, cantP, color, precioBase, marca)
        self.__patente = patente
        self.__anio = anio
        self.__kms = kms
    def getPatente(self):
        return self.__patente
    def getAnio(self):
        return self.__anio
    def getKilometraje(self):
        return self.__kms
    def getImpVenta(self):
        x = datetime.datetime.now().year
        if self.__kms < 100000:
            imp = float(self.getPrecioBase())-float(0.01*(x-self.__anio))
        else:
            imp = (float(self.getPrecioBase())-float(0.01*(x-self.__anio)))-(0.02*self.getPrecioBase())
        return imp 
    def __str__(self):
        return super().__str__() + " " + self.__patente + " " + str(self.__anio) + " " + str(self.__kms)