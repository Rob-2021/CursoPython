class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hablando...")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print (f"Hola, mi nombre es {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

Estudiante = Estudiante("Juan", 25, "Colombiano", 4.5, "Universidad Nacional")
print(Estudiante.nombre)

empleado_artista = EmpleadoArtista("Juan", 25, "Colombiano", "Cantar", 1000000, "Google")
empleado_artista.presentarse()

herencia = issubclass(EmpleadoArtista, Persona)
instancia = isinstance(empleado_artista, EmpleadoArtista)

print(instancia)
