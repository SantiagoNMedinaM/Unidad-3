import json
from pathlib import Path
from ClaseLista import Lista
from ClaseNodo import Nodo
from ClaseNuevo import Nuevo
from ClaseUsado import Usado
class ObjectEncoder(object):
    def decodificadorDiccionario(self,d):
        if "__class__" not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                listaV = class_()
                vehiculos = d['vehiculos']
                for i in range(len(vehiculos)):
                    dv = vehiculos[i]
                    class_name = dv.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dv["__atributos__"]
                    unV = class_(**atributos)
                    listaV.agregarV(unV)
        return listaV
    def leerArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:diccionario=json.load(fuente)
        fuente.close()
        return diccionario
    def guardar(self,d,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:json.dump(d,destino,indent=4)
        destino.close()
    #def convertirTextoADiccionario(self, texto):
        #return json.loads(texto)