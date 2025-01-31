# ejercicios_resueltos.py

# Ejercicio 1: Suma de los primeros N números naturales
def suma_naturales(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Ejercicio 2: Factorial de un número
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejercicio 3: Contar números pares en un rango
def contar_pares(a, b):
    contador = 0
    for num in range(a, b + 1):
        if num % 2 == 0:
            contador += 1
    return contador

# Ejercicio 4: Tabla de multiplicar de un número
def tabla_multiplicar(n, limite):
    resultados = []
    for i in range(1, limite + 1):
        resultados.append(n * i)
    return resultados

# Ejercicio 5: Verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ejercicio 6: Encontrar el máximo en una lista
def maximo_lista(lista):
    if not lista:
        return None
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

# Ejercicio 7: Invertir una cadena
def invertir_cadena(cadena):
    invertida = ""
    for char in cadena:
        invertida = char + invertida
    return invertida

# Ejercicio 8: Contar vocales en una cadena
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for char in cadena:
        if char in vocales:
            contador += 1
    return contador

# Ejercicio 9: Suma de dígitos de un número
def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

# Ejercicio 10: Generar la secuencia de Fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Ejercicio 11: Determinar si una palabra es palíndromo
def es_palindromo(palabra):
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - 1 - i]:
            return False
    return True

# Ejercicio 12: Calcular el promedio de una lista
def promedio_lista(lista):
    if not lista:
        return 0
    suma = 0
    for num in lista:
        suma += num
    return suma / len(lista)

# Ejercicio 13: Contar ocurrencias de un carácter en una cadena
def contar_caracter(cadena, caracter):
    contador = 0
    for char in cadena:
        if char == caracter:
            contador += 1
    return contador

# Ejercicio 14: Eliminar duplicados de una lista
def eliminar_duplicados(lista):
    sin_duplicados = []
    for elemento in lista:
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)
    return sin_duplicados

# Ejercicio 15: Encontrar números divisibles entre un divisor en un rango
def numeros_divisibles(a, b, divisor):
    divisibles = []
    for num in range(a, b + 1):
        if num % divisor == 0:
            divisibles.append(num)
    return divisibles

# Ejercicio 16: Sumar números impares en un rango
def suma_impares(a, b):
    suma = 0
    for num in range(a, b + 1):
        if num % 2 != 0:
            suma += num
    return suma

# Ejercicio 17: Convertir una lista de números a cadenas
def numeros_a_cadenas(lista):
    cadenas = []
    for num in lista:
        cadenas.append(str(num))
    return cadenas

# Ejercicio 18: Encontrar el mínimo en una lista
def minimo_lista(lista):
    if not lista:
        return None
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo

# Ejercicio 19: Concatenar elementos de una lista de cadenas
def concatenar_cadenas(lista):
    concatenada = ""
    for cadena in lista:
        concatenada += cadena
    return concatenada

# Ejercicio 20: Contar palabras en una cadena
def contar_palabras(cadena):
    contador = 0
    en_palabra = False
    for char in cadena:
        if char != " " and not en_palabra:
            contador += 1
            en_palabra = True
        elif char == " ":
            en_palabra = False
    return contador