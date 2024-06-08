import random
import matplotlib.pyplot as plt


# Задаємо верхнє обмеження
upper_limit = 10


# Генеруємо множину випадкових елементів, обмежених зверху числом 10
random_set = {random.randint(1, upper_limit) for _ in range(10)}
# random_set = {random.randint(1, upper_limit)}


# Виведення множини
print("Множина випадкових елементів:", random_set)
print("Обмеження зверху:", upper_limit)


# Створення множини
A = list(random_set)


# Візуалізація засобами matplotlib
plt.plot(A, [0] * len(A), "ro")  # 'ro' - червоні точки
plt.title("Обмежена множина")
plt.xlabel("Елементи множини")
plt.yticks([])  # Вимкнення відображення осі y
plt.show()
