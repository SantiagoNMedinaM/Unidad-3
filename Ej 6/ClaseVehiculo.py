class Vehiculo:
    __modelo: str
    __cantP: int
    __color: str
    __precioB: float
    __marca: str
    def __init__(self,modelo, cantP, color, precioBase, marca):
        self.__modelo = modelo
        self.__cantP = cantP
        self.__color = color
        self.__precioB = precioBase
        self.__marca = marca
    def getModelo(self):
        return self.__modelo
    def getCantPuertas(self):
        return self.__cantP
    def getColor(self):
        return self.__color
    def getPrecioBase(self):
        return self.__precioB
    def getMarca(self):
        return self.__marca
    def modPrecio(self,new):
        self.__precioB = new
        return self.__precioB
    def __str__(self):
        return self.__marca + " " + self.__modelo + " " + self.__color + " " + str(self.__cantP) + " Puertas\tPrecio base:"+ str(self.__precioB)
    