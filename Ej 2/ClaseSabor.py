class Sabor:
    __idSabor: int
    __ingredientes: str
    __nombsabor: str
    def __init__(self,id,ing,nomb):
        self.__idSabor = id
        self.__ingredientes = ing
        self.__nombsabor = nomb
    def getId(self):
        return self.__idSabor
    def getIngredientes(self):
        return self.__ingredientes
    def getNombre(self):
        return self.__nombsabor
    def __str__(self):
        return "ID:{}\tSabor:{}".format(self.__idSabor,self.__nombsabor)