"""
Fibonacci:
Genera los primeros n números de la secuencia Fibonacci, donde n es un número ingresado por el usuario.
"""


def fibonacchi_n(n):
    a = 1
    b = 1
    c = 0
    for i in range(0, n + 1):
        c = a + b
        a = b
        b = c

    print(c)


fibonacchi_n(10)


"""
Subcadena más larga sin repetir caracteres:
Dado un string, encuentra la subcadena más larga que no tenga caracteres repetidos.

Calculadora de expresiones:
Escribe un programa que evalúe una expresión matemática dada como string. Deberá soportar paréntesis, sumas, restas, multiplicaciones y divisiones.

Números primos:
Escribe una función que devuelva una lista de los primeros n números primos.

Buscador de archivos:
Crea un script que busque archivos con una extensión específica en un directorio y subdirectorios y los liste.

Simulador de agenda telefónica:
Implementa una agenda donde puedas añadir, editar, eliminar y buscar contactos. Los contactos deberán tener nombre, número de teléfono y email. Utiliza un diccionario para almacenar la información.

Algoritmo de Dijkstra:
Implementa el algoritmo de Dijkstra para encontrar el camino más corto en un grafo. Puedes representar el grafo como un diccionario.

Compresión RLE (Run-Length Encoding):
Escribe una función que implemente el algoritmo de compresión RLE. Por ejemplo, el string "AAABBBCCDAA" se convertiría en "3A3B2C1D2A".

Juego de la vida de Conway:
Implementa el "Juego de la vida" de John Conway. Es un autómata celular donde las células en una malla evolucionan en pasos de tiempo discretos dependiendo de un conjunto de reglas.
"""


# Fibonacci con Recursión:
# Implementa la secuencia de Fibonacci usando recursión.


def print_five_to_one(number: int) -> None:
    print(number)
    if number > 1:
        number -= 1
        print_five_to_one(number=number)


print_five_to_one(number=5)


def print_five_to_one_(num: int) -> None:
    if num > 0:
        print(num)
        print_five_to_one_(num - 1)


print_five_to_one_(5)
