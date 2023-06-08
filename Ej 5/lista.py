from ClaseNodo import Nodo
class Lista:
    __len: int
    __comienzo: Nodo
    def __init__(self):
        self.__len = 0
        self.__comienzo = None
    def insertarElem(self,empleado,indice):
        nuevonodo  = Nodo(empleado)
        if indice == 1:
            nuevonodo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevonodo
        else:
            temporal = self.__comienzo
            contador = 1
            while temporal:
                if contador + 1 == indice:
                    nuevonodo.setSiguiente(temporal.getSiguiente())
                    temporal.setSiguiente(nuevonodo)
                    break
                temporal = temporal.getSiguiente()
                contador += 1
        self.__len += 1
    def agregarElemento(self,empleado):
        nuevonodo = Nodo(empleado)
        if self.__comienzo == None:
            self.__comienzo = nuevonodo
        else:
            temporal = self.__comienzo
            while temporal.getSiguiente() is not None:
                temporal = temporal.getSiguiente()
            temporal.setSiguiente(nuevonodo)
        self.__len += 1
    def mostrarElemento(self, indice):
        temporal = self.__comienzo
        cont = 0
        while temporal:
            if cont + 1 == indice:
                return temporal.getDato()
            temporal = temporal.getSiguiente()
            cont+=1
    def getLen(self):
        return self.__len