import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()


# Перемістимо лівий і нижній стовпчики до x = 0 і y = 0 відповідно
ax.spines[["left", "bottom"]].set_position(("data", 0))


# Сховати верхню та праву лінію
ax.spines[["top", "right"]].set_visible(False)


# Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей
# Також вимкнемо відсікання (clip_on=False) стрілок
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# Додамо проміжні лінії
ax.grid(True, linestyle="-.")


# Сформуємо ряд значень x. 100 елементів від -5 до 5
x = np.linspace(-5, 5, 100, False)


# Функціональну залежність
ax.plot(x, -(2 / 3) * x - 1 / 3)


# Запускаємо малювання графіка
plt.show()
