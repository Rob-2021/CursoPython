class Animal:
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

hacer_sonido(gato)

print(perro.sonido())

# Duck Typing
# Es un estilo de programación que se centra en los métodos y atributos de un objeto en lugar de su tipo.
# Si un objeto camina como un pato y suena como un pato, entonces es un pato.
# En Python, el polimorfismo se logra a través de una técnica llamada Duck Typing.

# Enlaces dinamicos

# Enlaces estaticos

# Tipo real

# Tipo declarado
