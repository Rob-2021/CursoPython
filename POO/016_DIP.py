# Principio de inversión de dependencias (DIP)
# El principio de inversión de dependencias establece que las clases de alto nivel no deben depender de las clases de bajo nivel. Ambos deben depender de abstracciones.


# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #logica para verificar si la palabra existe en el diccionario
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self, texto):
#         #usamos el diccionario para verificar las palabras
#         pass

from abc import ABC, abstractclassmethod

class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        #logica para verificar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar si la palabra existe en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        #usamos el verificador para verificar las palabras
        pass

corrector = CorrectorOrtografico(Diccionario())