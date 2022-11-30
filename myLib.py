def bubble_sort(arr):
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


def calc(num1, num2, symb: str):
    if symb == "+":
        return num1 + num2
    if symb == "-":
        return num1 - num2
    if symb == "*":
        return num1 * num2
    if symb == "/":
        return num1 / num2
