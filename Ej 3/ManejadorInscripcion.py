from ClaseInscripcion import Inscripcion
import csv
class ManejaIns:
    __listainsc: list
    def __init__(self):
        self.__listainsc = []
    def agregar(self,insc):
        self.__listainsc.append(insc)
    def buscarTaller(self,dni):
        i = 0
        while i < len(self.__listainsc) and self.__listainsc[i].getPersonaDni() != dni:
            i+=1
        if i == len(self.__listainsc):
            return None
        else:
            self.__listainsc[i].mostrarTaller()

    def buscarInsc(self,id):
        print("{:<15}{:<30}{:<15}".format("Nombre","Direccion","DNI"))
        for insc in range(len(self.__listainsc)):
            if (int(id) == int(self.__listainsc[insc].getId())):
                print(self.__listainsc[insc].getPersona())
    def regPag(self,dni):
        i = 0
        while i < len(self.__listainsc) and dni != self.__listainsc[i].getPersonaDni():
            i += 1
        if i == len(self.__listainsc):
            return None
        else:
            self.__listainsc[i].setPago()
            print ("Se modifico el estado del pago. (Pago = {})".format(self.__listainsc[i].getPago()))

    def guardar(self):
        file = open("Inscripciones.csv",'w',newline='')
        writer = csv.writer(file)
        for inscripcion in self.__listainsc:
            dni = inscripcion.getPersonaDni()
            id = inscripcion.getId()
            fecha = inscripcion.getFecha()
            pago = inscripcion.getPago()
            newfila = [dni,id,fecha,pago]
            writer.writerow(newfila)
        file.close