def decorador(function):
    def funcion_modificada():
        print('Antes de llamar a la funcion')
        function()
        print('Despues de llamar a la funcion')
    return funcion_modificada

# def saludo():
#     print('Hola mundo')

# saludo_modificado = decorador(saludo)

@decorador
def saludo():
    print('Hola mundo')

saludo()