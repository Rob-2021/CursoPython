# File handling

import os

# .txt file

#txt_file = open("D:\Lenguajes\Python\CursoPython\Intermedio\my_file.txt")
txt_file = open('Intermedio/my_file.txt', 'w+') # leer y escribir
txt_file.write('Mi nombre es Brais\nMi apellido es Moure\n35 anios\nY mi lenguaje favorito es Python')

#print(txt_file.read())
#print(txt_file.read(10)) # leer los primeros 10 caracteres
#print(txt_file.readline()) # leer la primera linea
#print(txt_file.readlines()) # leer todas las lineas
for line in txt_file.readlines():
    print(line)

txt_file.write('\nAunque tambien c# es un buen lenguaje')
print(txt_file.readline())

txt_file.close() # cerrar el archivo

with open('Intermedio/my_file.txt', 'a') as my_other_file:
    my_other_file.write('\nY C++')

#os.remove('Intermedio/my_file.txt') # borrar el archivo

# .json file
import json

json_file = open('Intermedio/my_file.json', 'w+')

json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "C#", "C++"],
    "website": "https://moure.dev"
}

json.dump(json_test, json_file, indent=4) # indent=4 para que se vea bonito

json_file.close()

with open('Intermedio/my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line) 

json_dict = json.load(open('Intermedio/my_file.json')) # cargar el archivo json
print(json_dict)
print(type(json_dict))
print(json_dict['name'])

# .csv file

import csv

csv_file = open('Intermedio/my_file.csv', 'w+')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'surname', 'age', 'language', 'website'])
csv_writer.writerow(['Brais', 'Moure', 35, 'Python', 'https://moure.dev'])
csv_writer.writerow(['Ros', '', 2, 'C#', ''])

csv_file.close()

with open('Intermedio/my_file.csv') as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# .xlsx file

#import xlrd # pip install xlrd

# .xml file

import xml