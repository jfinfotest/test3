import unittest
import assessment  # Asegúrate de que assessment.py exista y sea importable


class TestFunctions(unittest.TestCase):

    def test_es_par(self):
        self.assertTrue(assessment.es_par(2))
        self.assertFalse(assessment.es_par(3))

    def test_es_positivo(self):
        self.assertTrue(assessment.es_positivo(1))
        self.assertFalse(assessment.es_positivo(-1))
        self.assertFalse(assessment.es_positivo(0))

    def test_es_bisiesto(self):
        self.assertTrue(assessment.es_bisiesto(2000))
        self.assertTrue(assessment.es_bisiesto(2024))
        self.assertFalse(assessment.es_bisiesto(1900))
        self.assertFalse(assessment.es_bisiesto(2022))

    def test_cadena_mas_larga(self):
        self.assertEqual(assessment.cadena_mas_larga("Hola", "Mundo"), "Mundo")
        self.assertEqual(assessment.cadena_mas_larga("Python", "Java"), "Python")
        self.assertEqual(assessment.cadena_mas_larga("Hola", "Hola"), "Igual longitud")

    def test_dia_de_la_semana(self):
        self.assertEqual(assessment.dia_de_la_semana(1), "Domingo")
        self.assertEqual(assessment.dia_de_la_semana(5), "Jueves")
        self.assertEqual(assessment.dia_de_la_semana(7), "Sábado")
        self.assertEqual(assessment.dia_de_la_semana(8), "Número inválido")

    def test_costo_total(self):
        self.assertEqual(assessment.costo_total(100), 100)
        self.assertEqual(assessment.costo_total(150), 135)

    def test_es_triangulo(self):
        self.assertTrue(assessment.es_triangulo(3, 4, 5))
        self.assertFalse(assessment.es_triangulo(1, 2, 5))

    def test_es_primo(self):
        self.assertTrue(assessment.es_primo(2))
        self.assertTrue(assessment.es_primo(7))
        self.assertFalse(assessment.es_primo(4))
        self.assertFalse(assessment.es_primo(1))

    def test_tipo_caracter(self):
        self.assertEqual(assessment.tipo_caracter("a"), "Vocal")
        self.assertEqual(assessment.tipo_caracter("b"), "Consonante")
        self.assertEqual(assessment.tipo_caracter("!"), "Símbolo")

    def test_calificacion_letra(self):
        self.assertEqual(assessment.calificacion_letra(95), "A")
        self.assertEqual(assessment.calificacion_letra(82), "B")
        self.assertEqual(assessment.calificacion_letra(70), "C")
        self.assertEqual(assessment.calificacion_letra(65), "D")
        self.assertEqual(assessment.calificacion_letra(50), "F")

    def test_calculadora_simple(self):
        self.assertEqual(assessment.calculadora_simple(2, 3, "+"), 5)
        self.assertEqual(assessment.calculadora_simple(5, 2, "-"), 3)
        self.assertEqual(assessment.calculadora_simple(4, 5, "*"), 20)
        self.assertEqual(assessment.calculadora_simple(10, 2, "/"), 5)
        self.assertEqual(assessment.calculadora_simple(10, 0, "/"), "Error: División por cero")

    def test_es_perfecto(self):
        self.assertTrue(assessment.es_perfecto(6))
        self.assertTrue(assessment.es_perfecto(28))
        self.assertFalse(assessment.es_perfecto(12))

    def test_es_palindromo(self):
        self.assertTrue(assessment.es_palindromo("anita lava la tina"))
        self.assertTrue(assessment.es_palindromo("radar"))
        self.assertFalse(assessment.es_palindromo("Hola mundo"))

    def test_es_fecha_valida(self):
        self.assertTrue(assessment.es_fecha_valida(1, 1, 2023))
        self.assertTrue(assessment.es_fecha_valida(29, 2, 2000))
        self.assertFalse(assessment.es_fecha_valida(31, 2, 2023))
        self.assertFalse(assessment.es_fecha_valida(1, 13, 2023))
        self.assertFalse(assessment.es_fecha_valida(1, 1, -1))

    def test_decimal_a_binario(self):
        self.assertEqual(assessment.decimal_a_binario(0), "0")
        self.assertEqual(assessment.decimal_a_binario(1), "1")
        self.assertEqual(assessment.decimal_a_binario(5), "101")
        self.assertEqual(assessment.decimal_a_binario(10), "1010")

    def test_romano_a_entero(self):
        self.assertEqual(assessment.romano_a_entero("I"), 1)
        self.assertEqual(assessment.romano_a_entero("V"), 5)
        self.assertEqual(assessment.romano_a_entero("X"), 10)
        self.assertEqual(assessment.romano_a_entero("L"), 50)
        self.assertEqual(assessment.romano_a_entero("C"), 100)
        self.assertEqual(assessment.romano_a_entero("D"), 500)
        self.assertEqual(assessment.romano_a_entero("M"), 1000)
        self.assertEqual(assessment.romano_a_entero("IV"), 4)
        self.assertEqual(assessment.romano_a_entero("IX"), 9)
        self.assertEqual(assessment.romano_a_entero("XL"), 40)
        self.assertEqual(assessment.romano_a_entero("XC"), 90)
        self.assertEqual(assessment.romano_a_entero("CD"), 400)
        self.assertEqual(assessment.romano_a_entero("CM"), 900)
        self.assertEqual(assessment.romano_a_entero("MCMXCIX"), 1999)

    def test_busqueda_binaria(self):
        lista = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(assessment.busqueda_binaria(lista, 5), 2)
        self.assertEqual(assessment.busqueda_binaria(lista, 13), 6)
        self.assertEqual(assessment.busqueda_binaria(lista, 2), -1)

    def test_fibonacci(self):
        self.assertEqual(assessment.fibonacci(10), None) # No hay un valor de retorno, solo imprime

    def test_mcd(self):
        self.assertEqual(assessment.mcd(12, 18), 6)
        self.assertEqual(assessment.mcd(48, 180), 12)

# Esto es crucial para que unittest funcione.  De lo contrario, no se ejecutará nada.
if __name__ == '__main__':
    unittest.main()
