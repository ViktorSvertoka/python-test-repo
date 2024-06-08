from sympy import *
import numpy as np


x = Symbol("x")
y = x**6 + 2 * x**5 - 30 * x**4 + 16 * x**3 - 12 * x**2 + x + 3


yprime = y.diff(x)
print(yprime)

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


# Сформуємо ряд значень x. 100 елементів від -1 до 4
x = np.linspace(-1, 4, 100, False)


# Функціональну залежність
ax.plot(x, 6 * x**5 + 10 * x**4 - 120 * x**3 + 48 * x**2 - 24 * x + 1)


# Запускаємо малювання графіка
plt.show()
