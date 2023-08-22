# Variables

from ctypes import addressof


my_string_variable = 'my string variable'
print(my_string_variable)

esto_es_un_int = 34
print(esto_es_un_int)

my_int_to_str_varible = str(esto_es_un_int)
print(my_int_to_str_varible)
print(type(my_int_to_str_varible))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable,my_bool_variable, my_int_to_str_varible)

print("este es el valor de: ", my_bool_variable)

# Funcion del sistema
print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = "Juan", "Mouse", "Mousedev", "35"
print("Me llamo:", name, surname, ".Mi edad es:", age, ".Y mi alias es:", alias)

#Inputs
"""
name = input('What is your name: ')
age = input ('How old are you? ')

print(name)
print(age)"""

# Cambiamos su tipo
name = 35
age = 'Juan'
print(name)
print(age)

# Forzando el tipo?
address: str = 'Mi direccion'
address = 32
print(type(address))