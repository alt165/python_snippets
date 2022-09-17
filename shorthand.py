import random
from collections import Counter
""" intercambiar valores de variables 
el metodo más común es intercambiar los valores utilizando
una variable auxiliar pero python tiene otro método
"""

a = 1
b = 2

""" intercambio """
a, b = b, a


""" Encadenar comparadores
Es posible juntar una comparacion de valores dentro de un rango
 de la forma en que se escribe una expresion matemática.
el me todo tradicional de escribir es
(0 < a and a < 10 )
 """
valor = 5
resultado = (0 < valor < 10)
""" Resultado tiene el valor True porque valor está en el rango  """
print(resultado)
valor = 11
resultado = (0 < valor < 10)
""" resultado ahora es False """
print(resultado)


""" Repetir un string
es posible repetir n veces un string utilizando * """

palabra = "abcde "
frase = palabra * 4
print(frase)


""" Invertir un string """
frase = frase[::-1]
print(frase)

""" condicion if dentro de un grupo de valores """
x = 5
if x in[0, 1, 2, 3, 4, 5]:
    print("x está en el grupo")

""" Usando la librería random podemos obtener
valores al azar entre una lista definida
para simular el lanzamiento de una moneda """
resultado = random.choice(["Cara", "Ceca"])
print(resultado)

""" Es posible unir los datos de una lista
en una sola lista en comun eligiendo el caracter
con el que se separan los elementos """
lista = ["Progamacion", "en", "lenguaje", "Python"]
lista_combinada = " ".join(lista)
print(lista_combinada)

""" Usando la clase Counter podemos ver si dos 
strings tienen los mismos elementos aunque estén
en distinto orden """
def es_anagrama(string1, string2):
  return Counter(string1) == Counter(string2)

print(es_anagrama("asdfg", "gdasf"))
print(es_anagrama("asdfg", "qwert"))

""" Transponer una matriz """
matriz = [[1, 2, 3], [4, 5, 6]]
print("Matriz original")
for fila in matriz:
    print(fila)

#transpose in a single line
matriz_transpuesta = zip(*matriz)

print("Matriz transpuesta")
for fila in matriz_transpuesta:
    print(list(fila))

""" Convertir dos listas en un diccionario """
def listas_a_diccionario(claves, valores):
    return dict(zip(claves, valores))

lista1 = [1, 2, 3, 4]
lista2 = ["uno", "dos", "tres", "cuatro"]

print(listas_a_diccionario(lista1, lista2))

""" Contar elementos de una lista """
lista = ["a", "a", "a", "b", "b", "c"]
print(Counter(lista))
lista="aaasedaea"
print(Counter(lista))

""" Es posible crear listas en las que los elementos
se agregan solo si cumplen una condicion """
# Lista con los primeros numeros impares entre 1 y 10
lista_impar = [numero for numero in range(10) if numero%2 != 0]

# Lista con los numeros elevados al cuadrado
lista_cuadrados = [numero * numero for numero in range(10)]

print("Los numeros impares son:", lista_impar)
print("Los diez primeros cuadrados son:", lista_cuadrados)

""" Eliminar duplicados de una lista """
lista = "aadeeedfae"
lista = list(set(lista))
print(lista)