# Exception Handling 

number_one = 5
number_two = 1
number_two = '1'

# try except

try:
    print(number_one + number_two)
    print('No se ha producido un error')
except:
    # Se ejecuta si se ha producido una excepcion
    print('Se ha producido un error')

# try except else finally

try:
    print(number_one + number_two)
    print('No se ha producido un error')
except:
    print('Se ha producido un error')
else: # Opcional
    # Se ejecuta si no se ha producido una excepcion
    print('La ejecucion continua correctamente')  
finally: # Opcional
    #Se ejecuta siempre
    print('La ejecucion continua')  

# Excepciones por tipo

try:
    print(number_one + number_two)
    print('No se ha producido un error')
except ValueError:
    # Se ejecuta si se ha producido una excepcion
    print('Se ha producido un ValuError')
except TypeError:
    # Se ejecuta si se ha producido una excepcion
    print('Se ha producido un TypeError')

# Captura de la informacion de la excepcion
    
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except ValueError as error:
    # Se ejecuta si se ha producido una excepcion
    print(error)
except Exception as exception:
    print(exception)