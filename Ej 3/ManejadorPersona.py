from ClasePersona import Persona
class ManePersona:
    def __init__(self):
        self.__listapers = []
    def registraPersona(self):
        nom = str(input("Ingrese el nombre de la persona a registrar: "))
        dir = str(input("Ingrese la direccion de la persona: "))
        dni = str(input("Ingrese el dni de la persona: "))
        instancia = Persona(nom,dir,dni)
        self.__listapers.append(instancia)
        return instancia
    def buscarPersona(self,ingdni):
        i = 0
        while i < len(self.__listapers) and self.__listapers[i].getDni() != ingdni:
            i+=1
        if i == len(self.__listapers):
            i = None
        return i