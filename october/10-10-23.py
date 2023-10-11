# This ejercices will be for practice the sintaxis on python.

# Data types:

"""
Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

def is_legal_age(age: int) -> bool:
    if age >= 18:
        return True
    return False

print(is_legal_age(17))

"""
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""

def is_password_same(user_password:str)-> bool:
    password = "PassworD"
    if user_password.lower() == password.lower():
        return True
    return False

print(is_password_same("PAssword"))

"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

def is_odd_or_even(number:int) -> str:
    if number % 2 == 0:
        return f"The number {number} is odd"
    return f"The number {number} is even"
    
print(is_odd_or_even(7))



"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

class User:
    def __init__(self, money_account, age, name) -> None:
        self.name: str = name
        self.money_account: int =  money_account
        self.age:int = age

class State:
    def is_legal_trubute_person(user: User) -> str:
        if user.age > 16 and user.money_account >= 1000:
            return f"The User {user.name} is a legal tribute person."
        return f"The User {user.name} is not a legal tribute person."

eulaloquita: User = User(name="Sara", money_account=200, age= 21)
print(State.is_legal_trubute_person(eulaloquita))
