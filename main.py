class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        # Виклик методу під час ініціалізації
        self.is_adult = self.__check_adulthood()

        # Приклад логування
        print(
            f"Створено Human: {self.name}, Вік: {self.age}, Дорослий: {self.is_adult}"
        )

    def say_hello(self) -> str:
        return f"Hello! I am {self.name}"

    def __check_adulthood(self) -> bool:
        return self.age >= 18


bill = Human("Bill")
print(bill.say_hello())
print(f"Вік: {bill.age}, Дорослий: {bill.is_adult}")

jill = Human("Jill", 20)
print(jill.say_hello())
print(f"Вік: {jill.age}, Дорослий: {jill.is_adult}")
