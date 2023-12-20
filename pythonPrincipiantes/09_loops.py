## Loops

# While

my_codition = 0

while my_codition < 10:
    print(my_codition)
    my_codition += 2 # my_codition = my_codition + 2
else: # Es opcional
    print('Mi condicion es mayor o igual que 10')

print('La ejecucion continua')

while my_codition < 20:
    my_codition += 1
    if my_codition == 15:
        print('se detiene la ejecucion')
        break
    print(my_codition)

print('La ejecucion continua')

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, 'Brais', 'Moure', 'Brais')

for element in my_tuple:
    print(element)

my_set = {'Brais', 'Moure', 35}

for element in my_set:
    print(element)

my_dict = {
    'Nombre':'Brais',
    'Apellido':'Moure', 
    'Edad':35, 
    'Lenguajes': {'Python', 'Swift', 'Kotlin'},
    1:1.77
    }

#for element in list(my_dict.values()):
for element in my_dict:
    print(element)
    if element == 'Edad':
        break
else:
    print('Se han terminado de iterar los elementos')


for element in my_dict:
    print(element)
    if element == 'Edad':
        continue
    print('Se ejecuta')
else:
    print('Se han terminado de iterar los elementos')