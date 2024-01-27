class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print("Llamando... desde un", self.modelo)

    def colgar(self):
        print("Colgando... desde un", self.modelo)

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nCamara: {self.camara}"
    
samsung = Celular("Samsung", "S20", "12MP")
iphone = Celular("Apple", "iPhone 12", "12MP")

samsung.llamar()