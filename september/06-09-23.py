# Inversión de cadena:
# Invierte una cadena de caracteres sin usar funciones predefinidas.

print(list("Hello World"))

def inverse_string(word:str)->str:
    to_list = list(word)
    inverse_list = []

    count = len(to_list) - 1
    while(count >= 0):
        inverse_list.append(to_list[count])
        count -= 1

    print(str(inverse_list))

inverse_string("Hello World")

# Palíndromos:
# Decide si una palabra o frase dada es un palíndromo (se lee igual al derecho que al revés, ignorando espacios, puntuación y capitalización).

def is_palindromo(word):
    j = len(word) - 1
    for i in range(0, len(word)):
        if word[i] != word[j]:
            print("No es palindromo")
            return
        j -= 1
    print("Es palindromo")

is_palindromo("anilinaa")
