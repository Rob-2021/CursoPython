# Principio abierto/cerrado (Open/Closed Principle)
# El principio abierto/cerrado establece que una clase debe estar abierta para su extensión, pero cerrada para su modificación.

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError
    

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando mensaje a {self.usuario.email}')

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f'Enviando SMS a {self.usuario.sms}')

class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f'Enviando whatsapp a {self.usuario.whatsapp}')