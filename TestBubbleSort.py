import myLib
import pytest


# Тест функции, которая производит математические операции
class TestBubbleSort:

    # Тестируем программу на коррктных данных.
    def test_on_correct_sign(self):
        list1 = [5, 3, 4, 3, -546, 555, 666666]
        assert myLib.bubble_sort(list1) == [-546, 3, 3, 4, 5, 555, 666666]

    # Тестируем программу на некорретных данных. Функция вызывает исключение ValueError.
    def test_on_negative_value(self):
        with pytest.raises(ValueError):
            myLib.bubble_sort([])
