from ClaseVehiculo import Vehiculo
class Nuevo(Vehiculo):
    __version:  str
    def __init__(self, modelo, cantP, color, precioBase, marca,version):
        super().__init__(modelo, cantP, color, precioBase, marca)
        self.__version = version
    def getVersion(self):
        return self.__version
    def getImpVenta(self):
        if self.__version is not "Full":
            imp = float(self.getPrecioBase())+float(0.1)
        else:
            imp = float(self.getPrecioBase())+float(0.1)+float(0.02)
        return imp 
    def __str__(self):
        return super().__str__() + " " + self.__version