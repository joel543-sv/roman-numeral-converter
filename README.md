import unittest
from src.roman_converter import decimal_to_roman  # Importaremos la función una vez que esté implementada

class TestRomanConverter(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(900), "CM")

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            decimal_to_roman(0)  # No hay números romanos para 0
        with self.assertRaises(ValueError):
            decimal_to_roman(4000)  # El rango máximo permitido es hasta 3999

if __name__ == "__main__":
    unittest.main()







     def decimal_to_roman(number):
    if number <= 0 or number > 3999:
        raise ValueError("El número debe estar entre 1 y 3999")
    
    roman_numerals = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }
    result = ""
    for value, symbol in roman_numerals.items():
        while number >= value:
            result += symbol
            number -= value
    return result
