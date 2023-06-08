import csv
from ClaseSabor import Sabor
class ManeSabores:
    __sabores: list
    def __init__(self):
        self.__sabores = []
    def openFile(self):
        file = open("sabores.csv")
        reader = csv.reader(file,delimiter=";")
        for row in reader:
            id = int(row[0])
            nomb = str(row[1])
            ing = str(row[2])
            a = Sabor(id,ing,nomb)
            self.__sabores.append(a)
        file.close
    def mostrar(self):
        for sabores in self.__sabores:
            print(sabores)

    def buscarSabor(self, idsabor):
        i = 0
        while (i<len(self.__sabores)) and (self.__sabores[i].getId() != idsabor):
            i += 1
        return None if i == len(self.__sabores) else self.__sabores[i]