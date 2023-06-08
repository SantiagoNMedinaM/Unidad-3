import datetime
class Inscripcion:
    __fechains: datetime
    __pago: bool
    __persona: object
    __taller: object
    def __init__(self,persona,taller,pago = False):
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller
        self.__fechains = datetime.datetime.now()
    def getFecha(self):
        return self.__fechains
    def getPago(self):
        return self.__pago
    def setPago(self):
        self.__pago = not self.__pago
        return self.__pago
    def __str__(self):
        cadena = 'Fecha de inscripcion: ' + self.__fechaInscripcion + '\n'
        cadena += str(self.__persona)
        cadena += str(self.__taller)
        return cadena
    
    def mostrarTaller(self):
        print("El taller de la persona ingresada es: {} y debe el monto {}".format(self.__taller.getNombre(), self.__taller.getMonto()))

    def getPersonaDni(self):
        return self.__persona.getDni()
    
    def getId(self):
        return self.__taller.getId()
    
    def getPersona(self):
        return self.__persona

   

        