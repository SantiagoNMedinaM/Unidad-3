import csv
from ClaseTaller import Taller
from ManejadorInscripcion import ManejaIns
from ManejadorPersona import ManePersona
from ClaseInscripcion import Inscripcion
from ClasePersona import Persona
import numpy as np
class ManeTaller:
    __len: int
    __cant: int
    __talleres = []
    __controlPersonas = ManePersona()
    __controlInscripciones = ManejaIns()

    def __init__(self):
        self.__len = 0
        self.__cant = 0
        self.__talleres =   np.empty(self.__len, dtype=Taller)

    def setDimension(self, dimension):
        self.__len = dimension
        self.__talleres = np.empty(self.__len, dtype=Taller)

    def abrirTalleres(self):
        file = open("Talleres.csv")
        reader = csv.reader(file,delimiter=";")
        band = True
        for fila in reader:
            if band:
                dimension = int(fila[0])
                self.setDimension(dimension)
                band = not band
            else:
                id = fila[0]
                nomb = fila[1]
                vac = int(fila[2])
                monto = fila[3]
                tal = Taller(id,nomb,vac,monto)
                self.__talleres[self.__cant] = tal
                self.__cant += 1
        file.close
        return self.__talleres
    def mostrarTalleres(self):
        for i in range(self.__len):
            print(self.__talleres[i])
    
    def inscribirPers(self):
        self.mostrarTalleres()
        id = int(input("Ingrese id del taller al que desea inscribirse: "))
        if self.__talleres[(id)-1].getVacantes() > 0:
            self.__talleres[id-1].restarVac()
            persona = self.__controlPersonas.registraPersona()
            inscribir = Inscripcion(persona,self.__talleres[id-1])
            self.__controlInscripciones.agregar(inscribir)
        else:
            print("No quedan vacantes para este taller")
    
    def consultar(self, dni):
        band = self.__controlPersonas.buscarPersona(dni)
        if band == None:
            print ("El dni ingresado no se encontro")
        else:
            self.__controlInscripciones.buscarTaller(dni)
    def consultarins(self,id):
        self.__controlInscripciones.buscarInsc(id)
    def regPago(self,dni):
        band = self.__controlPersonas.buscarPersona(dni)
        if band == None:
            print("El dni ingresado no se encontro.")
        else:
            self.__controlInscripciones.regPag(dni)
    def newfile(self):
        self.__controlInscripciones.guardar()


