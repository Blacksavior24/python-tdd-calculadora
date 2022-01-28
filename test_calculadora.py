import unittest
from calculadora import Calculadora

class TestBasicos(unittest.TestCase):
    def test_una_calculadora_nueva_inicia_en_cero(self):
        calc = Calculadora()
        self.assertEqual(0,calc.valor())

    def test_la_suma_de_2_mas_3_debe_dar_5(self):
        calc = Calculadora()
        calc.suma(2,3)
        self.assertEqual(5,calc.valor())
