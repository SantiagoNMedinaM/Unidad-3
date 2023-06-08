from ClaseLista import Lista
from ClaseObjectEncoder import ObjectEncoder
from menu import Menu
if __name__ == "__main__":
    vehiculos = Lista()
    jsonF = ObjectEncoder()
    diccionario = jsonF.leerArchivo("vehiculos (2).json")
    vehiculos = jsonF.decodificadorDiccionario(diccionario)
    menu = Menu()
    menu.opciones(vehiculos)