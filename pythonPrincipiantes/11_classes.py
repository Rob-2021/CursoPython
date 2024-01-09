# Classes

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'): # Constructor
        self.full_name = f'{name} {surname} ({alias})' # Propiedad Publica
        self.__name = name # Propiedad Privada
        self.__surname = surname # Propiedad Privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f'{self.full_name} esta caminando')

my_person = Person('Brais', 'Moure')
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person('Brais', 'Moure', 'MoureDev')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Hector de Leon (El loco de los perros)'
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)