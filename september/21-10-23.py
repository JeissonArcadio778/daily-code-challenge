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
        
    