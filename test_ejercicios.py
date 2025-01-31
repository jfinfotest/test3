# test_ejercicios.py
import unittest
from ejercicios import (
    suma_naturales,
    factorial,
    contar_pares,
    tabla_multiplicar,
    es_primo,
    maximo_lista,
    invertir_cadena,
    contar_vocales,
    suma_digitos,
    fibonacci,
    es_palindromo,
    promedio_lista,
    contar_caracter,
    eliminar_duplicados,
    numeros_divisibles,
    suma_impares,
    numeros_a_cadenas,
    minimo_lista,
    concatenar_cadenas,
    contar_palabras,
)

class TestEjercicios(unittest.TestCase):

    def test_suma_naturales(self):
        self.assertEqual(suma_naturales(5), 15)
        self.assertEqual(suma_naturales(0), 0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_contar_pares(self):
        self.assertEqual(contar_pares(1, 10), 5)
        self.assertEqual(contar_pares(3, 7), 2)

    def test_tabla_multiplicar(self):
        self.assertEqual(tabla_multiplicar(5, 3), [5, 10, 15])

    def test_es_primo(self):
        self.assertTrue(es_primo(2))
        self.assertFalse(es_primo(4))

    def test_maximo_lista(self):
        self.assertEqual(maximo_lista([1, 3, 7, 2]), 7)
        self.assertIsNone(maximo_lista([]))

    def test_invertir_cadena(self):
        self.assertEqual(invertir_cadena("hola"), "aloh")
        self.assertEqual(invertir_cadena(""), "")

    def test_contar_vocales(self):
        self.assertEqual(contar_vocales("hola"), 2)
        self.assertEqual(contar_vocales(""), 0)

    def test_suma_digitos(self):
        self.assertEqual(suma_digitos(123), 6)
        self.assertEqual(suma_digitos(0), 0)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(0), [])

    def test_es_palindromo(self):
        self.assertTrue(es_palindromo("radar"))
        self.assertFalse(es_palindromo("hola"))

    def test_promedio_lista(self):
        self.assertEqual(promedio_lista([1, 2, 3, 4]), 2.5)
        self.assertEqual(promedio_lista([]), 0)

    def test_contar_caracter(self):
        self.assertEqual(contar_caracter("hola", "a"), 1)
        self.assertEqual(contar_caracter("hola", "z"), 0)

    def test_eliminar_duplicados(self):
        self.assertEqual(eliminar_duplicados([1, 2, 2, 3]), [1, 2, 3])

    def test_numeros_divisibles(self):
        self.assertEqual(numeros_divisibles(1, 10, 2), [2, 4, 6, 8, 10])

    def test_suma_impares(self):
        self.assertEqual(suma_impares(1, 10), 25)

    def test_numeros_a_cadenas(self):
        self.assertEqual(numeros_a_cadenas([1, 2, 3]), ["1", "2", "3"])

    def test_minimo_lista(self):
        self.assertEqual(minimo_lista([1, 3, 7, 2]), 1)
        self.assertIsNone(minimo_lista([]))

    def test_concatenar_cadenas(self):
        self.assertEqual(concatenar_cadenas(["hola", " ", "mundo"]), "hola mundo")

    def test_contar_palabras(self):
        self.assertEqual(contar_palabras("hola mundo"), 2)
        self.assertEqual(contar_palabras(""), 0)


if __name__ == "__main__":
    unittest.main()