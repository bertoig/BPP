# El siguiente código devuelve una lista con el mayor número de cada lista introducida

ejemplo = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [100, 250, 43]]

resultado = [max(lista) for lista in ejemplo]

print("El resultado de la compresion de la lista es: ", resultado, "\n")


# El siguiente código devuelve una lista de los números primos incluidos dentro de 
# una lista de números.

ejemplo2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def es_primo(num):
    if num < 2: #si es menor de 2 no es primo, devolverá Falso
        return False
    for i in range(2, num): #un ciclo desde el 2 hasta el num de entrada
        if num % i == 0: #si el resto da 0 no es primo, devuelve Falso
            return False
    return True

resultado2 = list(filter(es_primo, ejemplo2))

print("Los numeros primos en la lista de prueba son: ", resultado2, "\n")