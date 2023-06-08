class Menu:
    __opciones: int
    def __init__(self):
        self.__opciones = 0
    def seleccionar(self,ls,lh):
        while self.__opciones != 6:
            print("Menu de opciones: ")
            print("1)- Registrar un helado vendido.")
            print("2)- Mostrar el nombre de los 5 sabores de helado más pedidos.")
            print("3)- Ingresar un número de sabor y estimar el total de gramos vendidos.")
            print("4)- Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos")
            print("5)- Determinar el importe total recaudado por la Heladería, por cada tipo de helado")
            print("6)- Salir")
            self.__opcion = (int(input("Ingrese una opcion: ")))

            if self.__opcion == 1:
                lh.pedido(ls)
            elif self.__opcion == 2:
                lh.masvendidos()
            elif self.__opcion == 3:
                ls.mostrar()
                idSabor = int(input("Ingrese el id del helado a buscar"))
                lh.estimado(idSabor)
            elif self.__opcion == 4:
                print("Tipos de helado: ")
                print("100gr\t150gr\t250gr\t500gr\t1000gr")
                th = int(input("Seleccione un tipo de helado (SOLO EL NUMERO DE GRAMOS)"))
                lh.tamanio(th)
            elif self.__opcion == 5:
                lh.imp()
