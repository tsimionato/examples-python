from calculadora import Calc


def _test_calc_soma():
    calc = Calc()

    calc.soma(2, 2)
    assert calc == 4


def _test_calc_subtracao():
    calc = Calc()

    assert calc == 2


def _test_calc_multiplicao():
    calc = Calc()

    assert calc == 6


def _test_calc_divisao():
    calc = Calc()

    assert calc == 2
