# Encapsulamiento

class MiClase:
    def __init__(self):
        self.__atributo_privado = 'Valor'

    def __hablar(self):
        print('Hablando')

objeto = MiClase()
print(objeto.__atributo_privado)