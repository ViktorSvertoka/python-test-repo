import matplotlib.pyplot as plt
from sympy import diff, symbols


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


# Сформуємо ряд значень x. 100 елементів від -2 до 2.


x, y = symbols("x y")
# Задаємо функцію
fx = x**6 + 2 * x**5 - 30 * x**4 + 16 * x**3 - 12 * x**2 + x + 3
# Обраховуємо похідну функції
dx = diff((fx))
k = []
n = []
l = []


for i in range(1000):
    j = (
        (i) * 0.001
    ) + 3  # Задаємо інтервал - починаючи від 3 - тисячу разів по одній тисячній - буде 1, тому перебір буде йти до 4.
    k.append(j)
    n.append(dx.subs(x, j))
    l.append(fx.subs(x, j))


ax.plot(k, n)
ax.plot(k, l)


# Запускаємо малювання графіка
plt.show()
