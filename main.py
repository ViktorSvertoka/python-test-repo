def my_function():
    print("Hello, world!")


f = my_function
f()


from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)


# Використання
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply)


from typing import Callable


def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base**exponent

    return inner


# Використання
square = power(2)
cube = power(3)

print(square(4))
print(cube(4))


from typing import Callable, Dict


# Визначення функцій
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base**exponent

    return inner


# Використання power для створення функцій square та cube
square = power(2)
cube = power(3)

# Словник операцій
operations: Dict[str, Callable] = {
    "add": add,
    "multiply": multiply,
    "square": square,
    "cube": cube,
}

# Використання операцій
result_add = operations["add"](10, 20)  # 30
result_square = operations["square"](5)  # 25

print(result_add)
print(result_square)
