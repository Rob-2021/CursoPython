# class Ave:
#     def volar(self):
#         return 'Estoy volando'
    
# class Pinguino(Ave):
#     def volar(self):
#         return 'No puedo volar'
    
# def hacer_volar(Ave):
#     return Ave.volar()

# print(hacer_volar(Pinguino()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return 'Estoy volando'
    
class AveNoVoladora(Ave):
    def volar(self):
        return 'No puedo volar'
    
class Pinguino(AveNoVoladora):
    pass

def hacer_volar(Ave):
    return Ave.volar()

print(hacer_volar(Pinguino()))