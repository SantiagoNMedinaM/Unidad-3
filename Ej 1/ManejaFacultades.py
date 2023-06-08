import csv
from ClaseCarrera import Carrera
from ClaseFacultad import Facultad
class Manejador:
    __facultades = list
    def __init__(self):
        self.__facultades = []
    def cargarLista(self):
        archivo = open("Facultades.csv")
        reader = csv.reader(archivo,delimiter=";")
        i = 0
        for fila in reader:
            if len(fila) == 5:
                print("a")
                cod = int(fila[0])
                nomb = str(fila[1])
                dir = str(fila[2])
                loc = str(fila[3])
                tel = str(fila[4])
                fac1 = Facultad(cod,nomb,dir,loc,tel)
                self.__facultades.append(fac1)
            else:
                print("b")
                codigo = int(fila[1])
                nombre = str(fila[2])
                fecha = str(fila[3])
                dur = str(fila[4])
                titulo = str(fila[5])
                carre = Carrera(codigo,nombre,fecha,dur,titulo)
                self.__facultades[int(fila[0])-1].addCarrera(carre)
    
    def muestrafac(self,codigo):
        i=0
        cont = 1
        while (i < len(self.__facultades) and (self.__facultades[i].getCod()!= codigo)):
            i+=1
        if i < len(self.__facultades):
            print("{}".format(self.__facultades[i].getNombre()))
            for carrera in self.__facultades[i].getCarreras():
                print("{}:{}, Duracion:{}".format(cont,carrera.getNombre(),carrera.getDuracion()))

    def muestracarr(self,carr):
        i = 0
        band = False
        while not band:
            c = self.__facultades[i].buscarCarr(carr)
            if c != None:
                self.__facultades[i].mostrarfacu(c)
                band = True
            i+=1
    def muestra(self):
        for i in range(len(self.__facultades)):
            print(self.__facultades[i].mostrar())
