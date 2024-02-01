class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

juan = Persona('Juan', 28)

nombre = juan.get_nombre()
print(nombre)

juan.set_nombre('Juan Carlos')

nombre = juan.get_nombre()
print(nombre)
