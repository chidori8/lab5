import myLib
import pytest


# Тест функции, которая производит математические операции
class TestCalc:

    # Тестируем программу на коррктных данных.
    def test_on_correct_sign(self):
        assert myLib.calc(3, 5, '*') == 15

    # Тестируем программу на некорретных данных. Функция вызывает исключение ZeroDivisionError.
    def test_on_div_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            myLib.calc(3, 0, '/')
