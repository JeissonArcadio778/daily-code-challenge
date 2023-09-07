"""
Secuencia de Fibonacci:
Genera los primeros n números de la secuencia de Fibonacci.

Número primo:
Dado un número n, determina si es un número primo.

Factorial de un número:
Encuentra el factorial de un número dado n.

Inversión de cadena:
Invierte una cadena de caracteres sin usar funciones predefinidas.

Palíndromos:
Decide si una palabra o frase dada es un palíndromo (se lee igual al derecho que al revés, ignorando espacios, puntuación y capitalización).

Máximo común divisor:
Encuentra el máximo común divisor (MCD) de dos números.

Mínimo común múltiplo:
Encuentra el mínimo común múltiplo (MCM) de dos números.

Ordenamiento de una lista:
Implementa el algoritmo de ordenamiento "bubble sort" (o burbuja) para ordenar una lista de 
números.

Búsqueda binaria:
Implementa el algoritmo de búsqueda binaria para encontrar un elemento en una lista ordenada.

Suma de subconjunto:
Dada una lista de números y un valor objetivo t, determina si hay un subconjunto de la lista que sume exactamente t.
"""


# Secuencia de Fibonnacci:
n = 10
a = 1
b = 1
c = 0
for i in range(0, n):
    c = a + b
    print(c)
    a = b
    b = c


# is prime 

def is_prime(num:int)-> bool:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            return False

    return is_prime

print(is_prime(7))

