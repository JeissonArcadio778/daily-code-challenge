

# Clase Estudiante:
# Crea una clase Estudiante que tenga atributos como nombre, edad y calificaciones. Incluye métodos para calcular el promedio de calificaciones y para mostrar la información del estudiante.

class Student:
    def __init__(self, name: str, age: int, notes: list) -> None:
        self.name = name
        self.age = age
        self.notes = notes

    def __str__(self) -> str:
        return f"{self.name} {self.age}"


student1: Student = Student(age=21, name='Eulaloquita', notes=[5.0, 2.2])

print(student1.notes)



# Ordenar lista:
# Dada una lista de números, ordénala manualmente utilizando el algoritmo de burbuja (bubble sort).


def bubble_sort(arr: list) -> None:
    n = len(arr)

    for i in range(n - 1):
        print(f"{i+1} Recorrido (i = {i})")
        for j in range(n - 1 - i):
            print("j =", j)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


import random 

random_numbers = [random.randint(0, 11) for i in range(0, 5)]

bubble_sort(random_numbers)

print(random_numbers)