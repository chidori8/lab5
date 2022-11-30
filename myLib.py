#Принимает list содержащий в себе числа
#Производится сортировка методом пузырьковой сортировки
#Возвращает отсортированный list
#Пример: [2, 5, 0, -5, 42] -> [-5, 0, 2, 5, 42]
import copy


def bubble_sort(list):
    arr = copy.deepcopy(list)
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True


#Принимает n
#Производится вычисление чисел Фибоначчи
#Возвращает list чисел Фибоначчи
#Пример: n = 5 -> [1, 1, 2, 3, 5]
def fibon(n):
    fib1 = 1
    fib2 = 1
    list1 = []
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        list1.append(fib2)
        i = i + 1
    return list1


#Принимает 2 числа, с которыми необходимо произвести вычисления и знак действия
#Возвращает результат вычислений
#Пример: 5, 1, + -> 6
def calc(num1, num2, symb: str):
    if symb == "+":
        return num1 + num2
    if symb == "-":
        return num1 - num2
    if symb == "*":
        return num1 * num2
    if symb == "/":
        return num1 / num2
