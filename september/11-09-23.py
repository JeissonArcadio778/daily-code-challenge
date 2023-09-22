"""


Número mayor y menor:
Dada una lista de números, encuentra el número más grande y el más pequeño sin usar las funciones max() y min().



Invertir lista:
Dada una lista, inviértela sin usar la función reverse() ni slicing.


Clase Estudiante:
Crea una clase Estudiante que tenga atributos como nombre, edad y calificaciones. Incluye métodos para calcular el promedio de calificaciones y para mostrar la información del estudiante.


Contar vocales:
Dado un texto, cuenta cuántas vocales tiene y muestra la cantidad de cada una.




"""


# Suma de elementos:

# Dada una lista de números, calcula y devuelve la suma de todos sus elementos utilizando un bucle for.

import random 
import functools


random_numbers = []

for i in range(0, 11):
    random_numbers.append(random.randint(0, 101))
    print(random_numbers[i])


def sum(a, b):
    return a + b
increment = lambda x: x + 1


sum_random_list = functools.reduce(lambda counter, item: counter + item, random_numbers)
print(sum_random_list)


# Número repetido:
# Dada una lista de números, identifica si existe algún número repetido y muestra cuál es.

print("-------------------------")
analized_numbers = []
numbers = [1,2,3,1,2,4]
for i in range(0, len(numbers)):
    if numbers[i] in analized_numbers:
        print(f"{numbers[i]} está repetido")
    else:
        analized_numbers.append(numbers[i])
        
print(analized_numbers)


# Invertir lista:
# Dada una lista, inviértela sin usar la función reverse() ni slicing.

analized_numbers_reverse = []
index_in_analized_numbers = len(analized_numbers) - 1

while (index_in_analized_numbers >= 0):
    print(analized_numbers[index_in_analized_numbers])
    analized_numbers_reverse.append(analized_numbers[index_in_analized_numbers])
    index_in_analized_numbers -= 1

print(analized_numbers_reverse)


# Filtro de palabras:
# Dada una lista de palabras, devuelve una nueva lista que contenga solo aquellas palabras que tienen 5 o más letras.

words = ['Hello World', 'I am Jeisson Arcadio', 'I tomc U', 'Think Twice, Code One', 'Sad']

# for word in words:
#     if len(word) >= 5:
#         print(word)


words_bigger_than_five = [word for word in words if len(word) >= 5]

print(words_bigger_than_five)
