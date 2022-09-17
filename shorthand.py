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
resultado = 11
resultado = (0 < valor < 10)
""" resultado ahora es False """
print(resultado)