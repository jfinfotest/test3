def es_par(numero):
    """
    Determina si un número dado es par.

    Args:
        numero: El número a evaluar.

    Returns:
        True si el número es par, False si es impar.
    """
    if numero % 2 == 0:
        return False
    else:
        return True

def es_positivo(numero):
    """
    Determina si un número dado es positivo.

    Args:
        numero: El número a evaluar.

    Returns:
        True si el número es positivo, False si es negativo o cero.
    """
    if numero > 0:
        return True
    else:
        return False

def es_bisiesto(año):
    """
    Determina si un año dado es bisiesto.

    Args:
        año: El año a evaluar.

    Returns:
        True si el año es bisiesto, False si no lo es.
    """
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

def cadena_mas_larga(cadena1, cadena2):
    """
    Dadas dos cadenas, imprime la cadena más larga. Si tienen la misma longitud, imprime "Igual longitud".

    Args:
        cadena1: La primera cadena.
        cadena2: La segunda cadena.

    Returns:
        La cadena más larga, o "Igual longitud" si ambas tienen la misma longitud.
    """
    if len(cadena1) > len(cadena2):
        return cadena1
    elif len(cadena1) < len(cadena2):
        return cadena2
    else:
        return "Igual longitud"

def dia_de_la_semana(numero):
    """
    Dado un número del 1 al 7, imprime el día de la semana correspondiente (1-Domingo, 2-Lunes, ..., 7-Sábado).

    Args:
        numero: El número que representa el día de la semana.

    Returns:
        El nombre del día de la semana, o "Número inválido" si el número no está en el rango.
    """
    dias = {
        1: "Domingo",
        2: "Lunes",
        3: "Martes",
        4: "Miércoles",
        5: "Jueves",
        6: "Viernes",
        7: "Sábado"
    }
    if numero in dias:
        return dias[numero]
    else:
        return "Número inválido"

def costo_total(precio):
    """
    Calcula el costo total de una compra. Si el total es mayor a $100, aplica un descuento del 10%.

    Args:
        precio: El precio original de la compra.

    Returns:
        El costo total después de aplicar el descuento (si corresponde).
    """
    if precio > 100:
        descuento = precio - 0.1
        return precio - descuento
    else:
        return precio

def es_triangulo(lado1, lado2, lado3):
    """
    Determina si tres longitudes dadas pueden formar un triángulo.

    Args:
        lado1: La longitud del primer lado.
        lado2: La longitud del segundo lado.
        lado3: La longitud del tercer lado.

    Returns:
        True si las longitudes pueden formar un triángulo, False si no.
    """
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        return True
    else:
        return False

def es_primo(numero):
    """
    Determina si un número dado es un número primo.

    Args:
        numero: El número a evaluar.

    Returns:
        True si el número es primo, False si no lo es.
    """
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def tipo_caracter(caracter):
    """
    Dado un carácter, determina si es una vocal, una consonante o un símbolo.

    Args:
        caracter: El carácter a evaluar.

    Returns:
        "Vocal" si es una vocal, "Consonante" si es una consonante, "Símbolo" si es un símbolo.
    """
    vocales = "aeiouAEIOU"
    if caracter in vocales:
        return "Vocal"
    elif caracter.isalpha():
        return "Consonante"
    else:
        return "Símbolo"

def calificacion_letra(calificacion):
    """
    Dada una calificación numérica (0-100), imprime la calificación de letra correspondiente (A, B, C, D, F).

    Args:
        calificacion: La calificación numérica.

    Returns:
        La calificación de letra correspondiente.
    """
    if calificacion >= 90:
        return "A"
    elif calificacion >= 80:
        return "B"
    elif calificacion >= 70:
        return "C"
    elif calificacion >= 60:
        return "D"
    else:
        return "F"

def calculadora_simple(num1, num2, operador):
    """
    Simula una calculadora simple. El usuario debe ingresar dos números y un operador (+, -, \*, /) y el programa debe imprimir el resultado.
    Maneja el caso de división por cero.

    Args:
        num1: El primer número.
        num2: El segundo número.
        operador: El operador (+, -, \*, /).

    Returns:
        El resultado de la operación.
    """
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/" and num2 != 0:
        return num1 / num2
    else:
        return "Error: División por cero"

def es_perfecto(numero):
    """
    Determina si un número dado es un número perfecto.

    Args:
        numero: El número a evaluar.

    Returns:
        True si el número es perfecto, False si no lo es.
    """
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    if suma_divisores == numero:
        return True
    else:
        return False

def es_palindromo(cadena):
    """
    Determina si una cadena dada es un palíndromo.

    Args:
        cadena: La cadena a evaluar.

    Returns:
        True si la cadena es un palíndromo, False si no lo es.
    """
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

def es_fecha_valida(dia, mes, año):
    """
    Dada una fecha (día, mes, año), determina si es una fecha válida.

    Args:
        dia: El día.
        mes: El mes.
        año: El año.

    Returns:
        True si la fecha es válida, False si no lo es.
    """
    if año < 0:
        return False
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        dias_mes[1] = 29
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_mes[mes - 1]:
        return False
    return True

def piedra_papel_tijera():
    """
    Simula un juego simple de "Piedra, Papel o Tijera" contra la computadora.

    Args:
        None

    Returns:
        None. Imprime el resultado del juego.
    """
    import random
    opciones = ["piedra", "papel", "tijera"]
    eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
    if eleccion_usuario not in opciones:
        print("Opción inválida.")
        return
    eleccion_computadora = random.choice(opciones)
    print(f"La computadora eligió: {eleccion_computadora}")
    if eleccion_usuario == eleccion_computadora:
        print("Empate!")
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

def decimal_a_binario(decimal):
    """
    Convierte un número decimal a binario.

    Args:
        decimal: El número decimal a convertir.

    Returns:
        La representación binaria del número decimal.
    """
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal //= 2
    return binario

def romano_a_entero(romano):
    """
    Convierte un número romano a un número entero.

    Args:
        romano: El número romano a convertir.

    Returns:
        El número entero correspondiente al número romano.
    """
    valores = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    entero = 0
    i = 0
    while i < len(romano):
        if i + 1 < len(romano) and valores[romano[i]] < valores[romano[i + 1]]:
            entero += valores[romano[i + 1]] - valores[romano[i]]
            i += 2
        else:
            entero += valores[romano[i]]
            i += 1
    return entero

def busqueda_binaria(lista, objetivo):
    """
    Implementa el algoritmo de búsqueda binaria para encontrar un elemento en una lista ordenada.

    Args:
        lista: La lista ordenada donde buscar.
        objetivo: El elemento a buscar.

    Returns:
        El índice del elemento en la lista si se encuentra, o -1 si no se encuentra.
    """
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def fibonacci(n):
    """
    Dado un número entero positivo, imprime la secuencia de Fibonacci hasta ese número.

    Args:
        n: El número hasta el que se imprimirá la secuencia.

    Returns:
        None. Imprime la secuencia de Fibonacci.
    """
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

def mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros utilizando el algoritmo de Euclides.

    Args:
        a: El primer número.
        b: El segundo número.

    Returns:
        El MCD de a y b.
    """
    while b:
        a, b = b, a % b
    return a
