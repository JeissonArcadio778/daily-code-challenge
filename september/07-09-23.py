"""
Máximo común divisor:
Encuentra el máximo común divisor (MCD) de dos números.

Mínimo común múltiplo:
Encuentra el mínimo común múltiplo (MCM) de dos números.
"""

def mcd(number1, number2):
    max_number_value = number1
    if number1 < number2: max_number_value = number2 

    divisors = []
    for i in range(1, max_number_value + 1):
        if number1 % i == 0 and number2 % i == 0:
            print(f"Divisor {i} del {number1} y {number2}")
            divisors.append(i)

    print(divisors)

mcd(12, 18)


def mcd(number1, number2):
    max_number_value = number1
    if number1 < number2: max_number_value = number2 

    divisors = []
    for i in range(1, max_number_value + 1):
        if number1 % i == 0 and number2 % i == 0:
            print(f"Divisor {i} del {number1} y {number2}")
            divisors.append(i)

    print(divisors)

mcd(12, 18)