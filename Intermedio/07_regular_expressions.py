# Expresiones Regulares
# Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda, principalmente utilizada para la búsqueda de patrones de cadenas de caracteres u operaciones de sustituciones.

import re

# match

my_string = 'Esta es la leccion numero 7: Leccion llamada Expresiones Regulares'
my_other_string = 'Esta no es la leccion numero 6: Manejo de ficheros'

match = re.match('Esta es la leccion', my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match('Esta no es la leccion', my_other_string)
#if not(match == None):
#if march is not None:
if match != None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

#print(re.match('Expresiones Regulares', my_string))

# search

search = re.search('leccion', my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall('leccion', my_string, re.I)
print(findall)

# split

split = re.split(':', my_string)
print(split)

# sub

sub = re.sub('Expresiones Regulares', 'RegEx', my_string)
print(sub)
sub = re.sub('[l|L]eccion', 'LECCION', my_string)
print(sub)

# Patterns
# Para aprender y validar expresiones regulares https://regex101.com

pattern = r'[lL]eccion'
print(re.findall(pattern, my_string))

pattern = r'[lL]eccion|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

# email validation regular expression
email = 'mouredev@mouredev.com'
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = 'mouredev@mouredev.com.mx'
print(re.findall(pattern, email))