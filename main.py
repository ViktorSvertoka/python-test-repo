def factorial(n):
    if n == 0:  # базовий випадок
        return 1
    else:
        return n * factorial(n - 1)  # рекурсивний випадок


print(factorial(5))  # виведе 120


def fibonacci(n):
    if n <= 1:  # базовий випадок
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # рекурсивний випадок


print(fibonacci(10))  # виведе 55


def stupid_recursion():
    stupid_recursion()


stupid_recursion()
