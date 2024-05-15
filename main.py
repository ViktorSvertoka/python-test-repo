class SmartCalculator:
    def __init__(self, operation="add"):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == "add":
            return a + b
        elif self.operation == "subtract":
            return a - b
        else:
            raise ValueError("Невідома операція")


add = SmartCalculator("add")
print(add(5, 3))  # 8

subtract = SmartCalculator("subtract")
print(subtract(10, 7))  # 3
