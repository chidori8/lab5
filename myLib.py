import copy


#Принимает list содержащий в себе числа
#Производится сортировка методом пузырьковой сортировки
#Возвращает отсортированный list
#Пример: [2, 5, 0, -5, 42] -> [-5, 0, 2, 5, 42]
#Классы эквивалентности: list - должен быть типом list
def bubble_sort(list1 : list):
    if list1 == []:
        raise ValueError
    arr = copy.deepcopy(list1)
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
    return arr


#Принимает n
#Производится вычисление чисел Фибоначчи
#Возвращает list чисел Фибоначчи
#Пример: n = 5 -> [1, 1, 2, 3, 5]
#Классы эквивалентности: n - натуральное число
#Граничные значения: n > 0
def fibon(n):
    if n < 0:
        raise IndexError
    i = 0
    fib1 = 1
    fib2 = 1
    list1 = [fib1, fib2]
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
#Классы эквивалентности: num1, num2 - числа; symb - символ
#Граничные значения: symb == ("+" || "-" || "/" || "*")
def calc(num1, num2, symb: str):
    if symb == "+":
        return num1 + num2
    if symb == "-":
        return num1 - num2
    if symb == "*":
        return num1 * num2
    if symb == "/":
        return num1 / num2

print(bubble_sort([5,3,4,3,-546,555,666666]))