# Condicionales

from pickle import TRUE


my_codition = False

if my_codition: # es lo mismo if conditional == True
    print('Se ejecuta la condicion del if')

my_codition = 5 * 5

if my_codition == 10:
    print('Se ejecuta la condicion del segundo if')

if my_codition > 10 and my_codition < 20:
    print('Es mayor que 10 y menor que 20')
elif my_codition == 25:
    print('Es igual a 25')
else:
    print('Es menor o igual que 10 o mayor o igual que 20')


print('La ejecucion continua')

my_string = ''

if not my_string:
    print('Mi cadena de texto es vacia')

if my_string == 'Micadena de textooooo':
    print('Estas cadenas de texto coinciden')