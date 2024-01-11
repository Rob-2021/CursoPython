# Funciones

def my_function():
    print('Esta es una funcion')

my_function()

def sum(first_number, second_number):
    print(first_number + second_number)

sum(5, 10)
sum('5', '10')
sum(1.4, 2.3)

def sum_with_return(first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

my_result = sum_with_return(5, 10)
print(my_result)

def print_name(name, surname):
    print(f'El nombre es {name} y el apellido es {surname}')

print_name(surname = 'Moure', name = 'Brais')

def print_name_with_default(name, surname, alias = 'Sin alias'):
    print(f'El nombre es {name} y el apellido es {surname} y el alias es {alias}')

print_name_with_default('Brais', 'Moure')
print_name_with_default('Brais', 'Moure', 'MoureDev')

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts('Hola', 'Mundo', 'Desde', 'Python')
print_upper_texts('hola')