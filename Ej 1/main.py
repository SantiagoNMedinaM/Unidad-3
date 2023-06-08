from ManejaFacultades import Manejador
from menu import MenuOpciones
if __name__ == "__main__":
    maneja = Manejador()
    maneja.cargarLista()
    maneja.muestra()
    menu = MenuOpciones()
    menu.opciones(maneja)
    
