from ManejadorTaller import ManeTaller
from ClaseMenu import Menu
if __name__ == "__main__":
        taller = ManeTaller()
        taller.abrirTalleres()
        m = Menu()
        m.opciones(taller)