import unittest
from calculadora import Calculadora

class TestBasicos(unittest.TestCase):
    def test_una_calculadora_nueva_inicia_en_cero(self):
        calc = Calculadora()
        self.assertEqual(0,calc.valor())

