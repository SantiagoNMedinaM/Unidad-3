from ClaseEmContratado import Contratado
from ClaseEmExterno import Externo
from ClaseEmPlanta import DePlanta
import numpy as np
import csv
class ManeEmpleados:
    __indice: int
    __len: int
    __empleados: object
    def __init__(self):
        self.__indice = 0
        self.__len = 0
        self.__empleados = None
    def setDimension(self,lenght):
        self.__len = lenght
        self.__empleados = np.empty(self.__len, dtype= object)
    def cargarArreglo(self):
        size = int(input("Ingrese la cantidad de empleados a almacenar: "))
        self.setDimension(size - 1)
        self.cargarDeplanta()
        self.cargarContratado()
        self.cargarExterno()
    def cargarDeplanta(self):
        band = True
        file = open("planta.csv")
        reader = csv.reader(file,delimiter=";")
        for row in reader:
            if band:
                band = False
            else:
                dni = row[0]
                nomb = row[1]
                dir = row[2]
                tel = row[3]
                sueldo = row[4]
                antiguedad = row[5]
                plant = DePlanta(dni,nomb,dir,tel,sueldo,antiguedad)
                if self.__indice < self.__len:
                    self.__empleados[self.__indice] = plant
                    self.__indice += 1
        file.close
        return self.__indice
    def cargarContratado(self):
        band = True
        file = open("contratados.csv")
        reader = csv.reader(file,delimiter=",")
        for row in reader:
            if band:
                band = False
            else:
                dni = row[0]
                nomb = row[1]
                dir = row[2]
                tel = row[3]
                fechain = row[4]
                fechafin = row[5]
                hstr = int(row[6])
                pp = row[7]
                cont = Contratado(dni,nomb,dir,tel,fechain,fechafin,hstr,pp)
                if self.__indice < self.__len:
                    self.__empleados[self.__indice] = cont
                    self.__indice += 1
        file.close
        return self.__indice
    def cargarExterno(self):
        band = True
        file = open("externos.csv")
        reader = csv.reader(file,delimiter=";")
        for row in reader:
            if band:
                band = False
            else:
                dni = row[0]
                nomb = row[1]
                dir = row[2]
                tel = row[3]
                tarea = row[4]
                fechain = row[5]
                fechafin = row[6]
                montoV = row[7]
                mdo = row[8]
                msv = row[9]
                ext = Externo(dni,nomb,dir,tel,tarea,fechain,fechafin,montoV,mdo,msv)
                if self.__indice < self.__len:
                    self.__empleados[self.__indice] = ext
                    self.__indice += 1
        file.close
        return self.__indice
    def buscarDni(self,dni):
        i = 0
        while i < len(self.__empleados) and self.__empleados[i].getDNI() != dni:
            i += 1
        if i == len(self.__empleados):
            i = None
        return i
    def registrar(self,pos,hs):
        print("Horas trabajadas antes de registrar las horas {}".format(self.__empleados[pos].getCantHs()))
        self.__empleados[pos].modificarHoras(hs)
        print("Horas trabajadas luego de registrar las horas {}".format(self.__empleados[pos].getCantHs()))
    def totalTarea(self,tarea,fecha):
        montot = 0
        for empleados in  self.__empleados:
            if isinstance(empleados,Externo) and empleados.getTarea() == tarea and str(empleados.getFechaFin) > str(fecha):
                montot += empleados.getSueldo()
        print ("El monto total a pagar para la tarea {}, es de {}$".format(tarea,montot))
    def ayudaEco(self):
        print("{:<20} {:<35} {:<20}".format("Nombre","Direccion","DNI"))
        for empleado in self.__empleados:
            if int(empleado.getSueldo()) < 150000:
                print("{:<20} {:<35} {:<20}".format(empleado.getNombre(),empleado.getDireccion(),empleado.getDNI()))
    def showAll(self):
        print("{:<20} {:<25} {:<15}".format("Nombre","Telefono","Sueldo"))
        for empleado in self.__empleados:
            print("{:<20} {:<25} {:<15}".format(empleado.getNombre(),empleado.getTelefono(),empleado.getSueldo()))


