try:
    # Код, який може викликати виняток
    result = 10 / 0
except ZeroDivisionError:
    # Обробка винятку ділення на нуль
    print("Ділення на нуль!")
except Exception as e:
    # Обробка будь-якого іншого винятку
    print(f"Виникла помилка: {e}")
else:
    # Виконується, якщо виняток не був викликаний
    print("Все пройшло успішно!")
finally:
    # Виконується завжди, незалежно від того, був виняток чи ні
    print("Блок finally завжди виконується.")


# Визначення власного класу винятку
class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
        self.message = message
        super().__init__(self.message)


# Функція для перевірки віку
def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи меньший за 18 років")


if __name__ == "__main__":
    # Обробка винятку
    try:
        verify_age(26)  # Змініть вік для різних результатів
    except AgeVerificationError as e:
        print(f"Виняток: {e}")
    else:
        print("Вік перевірено, особа доросла.")
