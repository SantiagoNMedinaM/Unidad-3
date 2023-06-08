class Helado:
    __gramos: float
    __precio: float
    __sabores: list
    def __init__(self,gr=0,precio=0):
        self.__gramos = gr
        self.__precio = precio
        self.__sabores = []
    def addSabor(self,sabor):
            self.__sabores.append(sabor)
    def getGramos(self):
        return self.__gramos
    def getPrecio(self):
        return self.__precio
    def getSabores(self):
        return self.__sabores
    def mostrarSabores(self):
        saborstr = ''
        for sabor in self.__sabores:
            saborstr += str(sabor) + ' '
        return saborstr
    def __str__(self):
         return "Gramos: " + str(self.__gramos) + "\t" + "Precio: " +str(self.__precio) + "\t" + "Sabores: " + self.mostrarSabores() 
    def estimarGr(self):
         gr = self.__gramos/(len(self.__sabores))
         return gr