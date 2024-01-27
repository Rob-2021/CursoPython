class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

Juan = Estudiante("Juan", 25, "10mo")
Juan.mostrar_datos()
Juan.mostrar_grado()

####################################################

class Animal:
    def comer(self):
        print("El animal esta comiendo...")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando...")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando...")

class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()