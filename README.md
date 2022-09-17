# python_snippets
Trozos de codigo en pyhton
---
Pequeños códigos de prueba en python que resuelven solo un problema puntual
para experimentar diferentes funcionalidades del lenguaje.
---
## Medir el tiempo de ejecución de un código.
### timeit
Este método mide el tiempo de ejecución de un trozo de código. La librería ejecuta el código un millón de veces y devuelve el menor tiempo de ejecución de estas instrucciones. 
```
    timeit.timeit(stmt, setup,timer, number)
```
Parametros:

- stmt: Este es el código que se quiere medir. El valor por defecto es “pass”.
- setup: Acá van los detalles del setup que se ejecutan antes de stmt. The default value is “pass.”
- timer: Este es el valor del timer, timeit() viene con un valor precargado y se puede ignorar.
- number: Esta es la cantidad de veces que se ejecutará el código. el valor por defecto es 1000000.

Para utilizar este metodo hay que importar **timeit**.

---

### Pyhton shorthand
En este archivo hay atajos simples con algunas particularidades de python que permiten resolver
de una forma distinta problemas comunes de programacion.
Loe ejemplos son:
- Intercambiar valores.
- Encadenar comparadores.
- Repetir string n veces.
- Invertir string.
- if in grupo.

