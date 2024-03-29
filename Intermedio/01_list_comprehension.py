# List Comprehension
# List comprehension es una forma de crear listas de forma sencilla y rápida

my_origin_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_origin_list)

my_range = range(8)
print(list(my_range))

my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)