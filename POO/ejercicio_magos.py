class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        # print(f'Nombre: {self.nombre}')
        print(f'{self.nombre}:')
        print(f'-Fuerza: {self.fuerza}')
        print(f'-Inteligencia: {self.inteligencia}')
        print(f'-Defensa: {self.defensa}')
        print(f'-Vida: {self.vida}')

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f'{self.nombre} ha muerto')

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f'{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}')
        if enemigo.esta_vivo():
            print(f'La vida de {enemigo.nombre} es {enemigo.vida}')
        else:
            enemigo.morir()

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input('elige un arma: (1) Acero Valyrio, daño 8 (2) Matadragones, daño 10 '))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print('Numero de arma incorrecto')

    def atributos(self):
        super().atributos()
        print(f'-Espada: {self.espada}')

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f'-Libro: {self.libro}')

    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

mi_personaje = Personaje('Gandalf', 20, 15, 10, 100)
# mi_enemigo = Personaje('Sauron', 8, 5, 3, 5)           
guts = Guerrero('Guts', 20, 10, 4, 100, 4)
venessa = Mago('Venessa', 5, 15, 4, 100, 3)

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print('\nTurno', turno + 1)
        print(f'Accion de {jugador_1.nombre}')
        jugador_1.atacar(jugador_2)
        print(f'Accion de {jugador_2.nombre}')
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print(f'{jugador_1.nombre} ha ganado')
    elif jugador_2.esta_vivo():
        print(f'{jugador_2.nombre} ha ganado')
    else:
        print('\nEmpate')

combate(guts, venessa)

