# Python Package Manager
# pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.

import numpy as np

print(np.__version__)

numpy_array = np.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

#import pandas as pd

# pip list
# pip uninstall numpy
# pip show numpy

import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
print(response.json())

# Arithmetic Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))