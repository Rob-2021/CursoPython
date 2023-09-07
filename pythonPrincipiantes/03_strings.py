# Strings

my_string = 'mi string'
my_other_string = "mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String \ncon salto de linea"
print(my_new_line_string)

mi_tab_string = "\tEste es un String con tabulacion"
print(mi_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = 'Juan', 'Vaca', 35

print("Mi Nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi Nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi Nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

lenguaje = 'Python'
a, b, c, d, e, f = lenguaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division

language_slice = lenguaje[1:3]
print(language_slice)

language_slice = lenguaje[1:]
print(language_slice)

language_slice = lenguaje[-2]
print(language_slice)

# Reverse

reverse_language = lenguaje[::-1]
print(reverse_language)
