class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: ")) 
grado = input("Ingrese el grado del estudiante: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"Nombre: {estudiante.nombre}\nEdad: {estudiante.edad}\nGrado: {estudiante.grado}")

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()