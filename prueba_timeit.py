# prueba modulo timeit
import timeit

# definir import para setup
import_setup = "import random"

# codigo a evaluar
codigo = '''
def factorial():
    j = random.randint(1, 10)
    i = 1
    while i < j:
        i = i * i
        i = i + 1
    return i
'''
print(timeit.timeit(stmt=codigo, setup=import_setup))