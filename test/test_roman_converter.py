# joel reynoso

import unittest
from src.roman_converter import decimal_to_roman  # Importaremos la función una vez que esté implementada

class TestRomanConverter(unittest.TestCase):
    # Pruebas para números básicos
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")

    # Pruebas para las reglas de sustracción
    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(900), "CM")

    # Pruebas para números complejos
    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

    # Pruebas para números fuera del rango permitido
    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            decimal_to_roman(0)  # No hay números romanos para 0
        with self.assertRaises(ValueError):
            decimal_to_roman(4000)  # El rango máximo permitido es hasta 3999

if __name__ == "__main__":
    unittest.main()
