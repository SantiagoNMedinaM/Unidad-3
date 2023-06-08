class Empleado:
    __dni=str
    __nombre=str
    __direccion=str
    __telefono=str

    def __init__(self,dni,nombre,direccion,telefono):
        self.__dni=dni
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono

    def __str__(self):
        return '{} {} {} {}'.format(self.__dni,self.__nombre,self.__direccion,self.__telefono)