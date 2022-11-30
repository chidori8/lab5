import myLib
import pytest


# Тест функции, которая производит математические операции
class TestFib:

    # Тестируем программу на коррктных данных.
    def test_on_correct_sign(self):
        assert myLib.fibon(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    # Тестируем программу на некорретных данных. Функция вызывает исключение IndexError.
    def test_on_negative_value(self):
        with pytest.raises(IndexError):
            myLib.fibon(-50)
