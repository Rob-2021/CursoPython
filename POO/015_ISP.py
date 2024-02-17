# Principio de segregación de interfaces (ISP)
# El principio de segregación de interfaces establece que una clase no debe depender de métodos que no utiliza.

from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print('El humano esta Comiendo')
    
    def trabajar(self):
        print('El humano esta Trabajando')
    
    def dormir(self):
        print('El humano esta Durmiendo')

class Robot(Trabajador):
    def trabajar(self):
        print('El robot esta Trabajando')

robot = Robot()
humano = Humano()

robot.trabajar()
humano.comer()
humano.trabajar()