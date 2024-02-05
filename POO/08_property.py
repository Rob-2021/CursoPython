class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre
        
juan = Persona('Juan', 25)

nombre = juan.nombre
print(nombre)

juan.nombre = 'Pepe'

nombre = juan.nombre
print(nombre)

del juan.nombre # No se puede usar porque ya se uso el decorador @deleter

print('hola mundo')