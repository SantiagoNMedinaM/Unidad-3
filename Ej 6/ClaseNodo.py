from ClaseNuevo import Nuevo
from ClaseUsado import Usado
class Nodo:
    __vehiculo: object
    __siguiente: object
    def __init__(self,vehiculo):
        self.__vehiculo = vehiculo
        self.__siguiente = None
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__vehiculo
    def getModelo(self):
        return self.__vehiculo.getModelo()
    def getCantPuertas(self):
        return self.__vehiculo.getCantPuertas()
    def getColor(self):
        return self.__vehiculo.getColor()
    def getPrecioBase(self):
        return self.__vehiculo.getPrecioBase()
    def getMarca(self):
        return self.__vehiculo.getMarca()
    def modPrecio(self,new):
        return self.__vehiculo.modPrecio(new)
    def getPatente(self):
        if isinstance(self.__vehiculo, Usado):
            return self.__vehiculo.getPatente()
        else:
            return False
    def getAnio(self):
        if isinstance(self.__vehiculo, Usado):
            return self.__vehiculo.getAnio()
        else:
            return False
    def getKilometraje(self):
        if isinstance(self.__vehiculo, Usado):
            return self.__vehiculo.getKilometraje()
        else:
            return False
    def getImpVenta(self):
        return self.__vehiculo.getImpVenta()
    def getVersion(self):
        if isinstance(self.__vehiculo,Nuevo):
            return self.__vehiculo.getVersion()
        else:
            return False
    def toJSON(self):
        if isinstance(self.__vehiculo,Usado):
            d = dict(__class__=self.__class__.__name__,__atributos__=dict(marca=self.__vehiculo.getMarca(),modelo=self.__vehiculo.getModelo(),cantP=self.__vehiculo.getCantPuertas(),color=self.__vehiculo.getColor(),preciob=self.__vehiculo.getPrecioBase(),patente=self.__vehiculo.getPatente(),anio=self.__vehiculo.getAnio(),kms=self.__vehiculo.getKilometraje()))
        elif isinstance(self.__vehiculo,Nuevo):
            d = dict(__class__=self.__class__.__name__,__atributos__= dict(marca=self.__vehiculo.getMarca(),modelo=self.__vehiculo.getModelo(),cantP=self.__vehiculo.getCantPuertas(),color=self.__vehiculo.getColor(),preciob=self.__vehiculo.getPrecioBase(),version=self.__vehiculo.getVersion()))
        return d