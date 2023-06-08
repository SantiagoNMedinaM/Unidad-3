from ManejaSabores import ManeSabores
from ClaseHelado import Helado
from collections import Counter
class ManeHelado:
    __helados: list
    def __init__(self):
        self.__helados = []
    def pedido(self,sabores):
        print("Tipos de helado: 100gr, 150gr, 250gr, 500gr, 1000gr")
        gr=float(input("Ingrese el tipo de helado "))
        precio = float(input("Ingrese el precio del helado "))
        a = Helado(gr,precio)
        cantsabor = int(input("Ingrese la cantidad de sabores "))
        sabores.mostrar()
        for i in range(cantsabor):
            idsabor = int(input("Seleccione un sabor por su ID "))
            sabor = sabores.buscarSabor(idsabor)
            a.addSabor(sabor)
        self.__helados.append(a)

    def masvendidos(self):
        print("Sabores de helado mas pedidos: ")
        saboresContador = Counter()
        for helado in self.__helados:
            for sabor in helado.getSabores():
                    saboresContador[sabor] += 1
        saboresOrdenados = saboresContador.most_common(5)
        for sabor, contador in saboresOrdenados:
                print("{}: {} veces".format(sabor, contador))

    def estimado(self,idS):
        cont = 0
        for helado in self.__helados: 
            for sabor in helado.getSabores():
                 if (sabor.getId() == idS):
                    cont += helado.estimarGr()
        print("El sabor {}, tiene {}grs vendidos".format(idS,cont))

    def tamanio(self,th):
         print("Sabores vendidos para el tipo el helado de {}gr".format(th))
         sabmostr = ""
         for helado in self.__helados:
              if th == helado.getGramos():
                for sabor in helado.getSabores():
                   if sabor.getNombre() not in sabmostr:
                    print(sabor.getNombre())
                    sabmostr += sabor.getNombre() + ","
    def imp(self):
        impcien = 0
        impciencinco = 0
        impdoscinco = 0
        impquin = 0
        impmil = 0
        for helado in range(len(self.__helados)):
            if self.__helados[helado].getGramos() == 100:
                impcien += self.__helados[helado].getPrecio()
            if self.__helados[helado].getGramos() == 150:
                impciencinco += self.__helados[helado].getPrecio()
            if self.__helados[helado].getGramos() == 250:
                impdoscinco += self.__helados[helado].getPrecio()
            if self.__helados[helado].getGramos() == 500:
                impquin += self.__helados[helado].getPrecio()
            if self.__helados[helado].getGramos() == 1000:
                impmil += self.__helados[helado].getPrecio()
        print("La recaudación para el tipo {}gr es: {}".format(100, impcien))
        print("La recaudación para el tipo {}gr es: {}".format(150, impciencinco))
        print("La recaudación para el tipo {}gr es: {}".format(250, impdoscinco))
        print("La recaudación para el tipo {}gr es: {}".format(500, impquin))
        print("La recaudación para el tipo {}gr es: {}".format(1000, impmil))