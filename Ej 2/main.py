from ManejaHelados import ManeHelado
from ManejaSabores import ManeSabores
from ClaseMenu import Menu
if __name__ == "__main__":
    lh = ManeHelado()
    ls = ManeSabores()
    ls.openFile()
    m = Menu()
    m.seleccionar(ls,lh)

