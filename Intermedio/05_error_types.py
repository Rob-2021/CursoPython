# Error types

# Syntax error
#print "Hello world" # Error de sintaxis
print("Hello world")

# NameError
#print(my_variable) # Error de nombre
my_variable = 1
print(my_variable)

# IndexError
my_list = [1, 2, 3]
#print(my_list[3]) # Error de índice
print(my_list[2])

# ModuleNotFoundError
#import maths # Error de módulo
import math

# AttributeError
#print(math.PI) # Error de atributo
print(math.pi)

# KeyError
my_dict = {'name': 'Juan', 'age': 25, 'country': 'Colombia', 'city': 'Bogotá'}
print(my_dict['name'])
#print(my_dict['last_name']) # Error de llave

# TypeError
#print(my_list['0']) # Error de tipo
print(my_list[0])

# ImportError
#from math import PI # Error de importación
from math import pi
print(pi)

# ValueError
#print(int('a')) # Error de valor
print(int('1'))

# ZeroDivisionError
#print(1/0) # Error de división por cero
print(4/2)