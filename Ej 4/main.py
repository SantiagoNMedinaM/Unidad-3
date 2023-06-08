from ManejadorEmpleados import ManeEmpleados
from ClaseMenu import Menu
if __name__ == "__main__":
    emps = ManeEmpleados()
    emps.cargarArreglo()
    menuo = Menu()
    menuo.opciones(emps)