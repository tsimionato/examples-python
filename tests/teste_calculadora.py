# tests/test_calculadora.py
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.Caculadora.calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):
        resul = self.calc.soma(5, 3)
        self.assertEqual(resul, 8)

    def test_subtracao(self):
        resul = self.calc.subtracao(5, 3)
        self.assertEqual(resul, 2)

    def test_multiplicacao(self):
        resul = self.calc.multiplicacao(5, 3)
        self.assertEqual(resul, 15)

    def test_divisao(self):
        resul = self.calc.divisao(6, 3)
        self.assertEqual(resul, 2)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divisao(5, 0)


if __name__ == '__main__':
    unittest.main()
