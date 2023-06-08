from claseEmpleado import Empleado
import numpy as np
from interface import IEmpleado
from lista import Lista
from claseEmpleadoError import Error
class Manejador(IEmpleado):
    __lista = Lista()
    __len: int
    def __init__(self) -> None:
        self.__lista = Lista()
        self.__len = self.__lista.getLen()
    def insertarElem(self, empleado, indice):
        if indice <= 0:
            raise Error(self,"No se puede insertar un elemento en una lista en una posicion menor a 0")
        if indice > self.__len:
            raise Error(self,"No se puede agregar un elemento en una posicion mayor al tamaño de la lista")
        self.__lista.insertarElem(empleado,indice)
        print ("Elemento insertado")
    def agregarElemento(self, empleado):
        self.__lista.agregarElemento(empleado)
    def mostrarElemento(self, indice):
        if indice <= 0:
            raise Error(self,"No se puede mostrar un elemento de una lista en una posicion menor a 0")
        if indice > self.__len:
            raise Error(self,"No se puede mostrar un elemento de una lista en una posicion mayor del tamaño de la lista")
        print("{}".format(self.__lista.mostrarElemento(indice)))