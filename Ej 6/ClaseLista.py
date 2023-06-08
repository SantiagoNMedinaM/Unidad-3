from ClaseNuevo import Nuevo
from ClaseUsado import Usado
from ClaseInterface import IVehiculo
from zope.interface import implementer
from ClaseNodo import Nodo
import json
from ClaseException import PosicionInvalidaException
@implementer(IVehiculo)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __tope: int
    __ind: int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__ind = 0
    def agregarV(self, vehi):
        nodo = Nodo(vehi)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope +=1 

    def insertarElemento(self, vehiculo, posicion):
        nuevo = Nodo(vehiculo)
        contador = 0
        if posicion < 0 or posicion > self.__tope:
            raise PosicionInvalidaException("La posicion no es valida")
        else:
            if self.__comienzo == None:
                nuevo.setSiguiente(self.__comienzo)
                self.__comienzo = nuevo
                self.__actual = nuevo
            elif contador + 1 == posicion:
                nuevo.setSiguiente(self.__comienzo)
                self.__comienzo = nuevo
                self.__actual = nuevo
            else:
                aux = self.__comienzo
                ant = self.__comienzo
                while aux != None and contador < posicion:
                    ant = aux
                    aux = aux.getSiguiente()
                    contador += 1
                ant.setSiguiente(nuevo)
                nuevo.setSiguiente(aux)
                self.__actual = nuevo
                self.__tope += 1
    def existePatente(self,pat):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getPatente() == pat:
                band = True
            aux = aux.getSiguiente()
        return band
    def modificaPrecio(self,ingpat, nuevoprecio):
        aux = self.__comienzo
        while aux != None and ingpat != aux.getPatente():
            aux = aux.getSiguiente()
        if aux != None:
            aux.modPrecio(nuevoprecio)
    def mostrarValor(self,ingpat):
        aux = self.__comienzo
        while aux != None and ingpat != aux.getPatente():
            aux = aux.getSiguiente()
        if aux != None:
            print("El nuevo precio de venta del auto es:{}".format(aux.getImpVenta()))
    def masEconomico(self):
        aux = self.__comienzo
        min = 100000000000000000000
        while aux != None:
            if aux.getImpVenta() < min:
                min = aux.getImpVenta()
                autoaux = aux
            aux = aux.getSiguiente()
        print("El auto mas economico es: {}".format(autoaux.getDato(),autoaux.getImpVenta()))
    
    def vehiculosConcesionaria(self):
        aux = self.__comienzo
        while aux != None:
            print("{:<20}{:<20}{:<20}".format(aux.getModelo(),aux.getCantPuertas(),aux.getImpVenta()))
            aux = aux.getSiguiente()
    def mostrarElemento(self,posicion):
        c = 0
        aux = self.__comienzo
        if posicion < 0 or posicion > self.__tope:
            raise PosicionInvalidaException("Posicion invalida")
        else:
            while c != posicion and aux != None:
                aux = aux.getSiguiente()
                c+=1
            if posicion == c:
                print(aux.getDato())
            else:
                print("Esa posicion no se encuentra dentro de la lista")
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__ind == self.__tope:    
            self.__actual = self.__comienzo
            self.__ind = 0
            raise StopIteration
        else:
            self.__ind += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    def toJSON(self):
        aux = self.__comienzo
        ld = []
        while aux != None:
            vdic = aux.toJSON()
            ld.append(vdic)
            aux = aux.getSiguiente()
        return ld
    
    def mostrarLista(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()




