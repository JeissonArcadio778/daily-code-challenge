"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

def investor(amount:float, interest: float, years: int) -> float:
    return amount * ( 1 + interest/ 100) ** years

print(investor(100, 2, 2))