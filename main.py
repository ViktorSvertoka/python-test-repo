import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# Задаємо функцію
def func(x):
    return (x - 3) * (x - 5) * (x - 7) + 85


# Границі інтегрування
a, b = 2, 9  # integral limits
# Діапазон зміни x
x = np.linspace(0, 10)
# Розраховуємо значення y
y = func(x)


fig, ax = plt.subplots()
ax.plot(x, y, "r", linewidth=2)
ax.set_ylim(bottom=0)


# Оформлюємо область
# Генеруємо значення x та y в області інтегрування
ix = np.linspace(a, b)
iy = func(ix)


# Зафарбовуємо область
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor="0.9", edgecolor="0.5")
ax.add_patch(poly)


# Розміщуємо текст інтеграла всередині області
ax.text(
    0.5 * (a + b),
    30,
    r"$\int_a^b f(x)\mathrm{d}x$",
    horizontalalignment="center",
    fontsize=20,
)


# Підписуємо осі
fig.text(0.9, 0.05, "$x$")
fig.text(0.1, 0.9, "$y$")


# Ховаємо верхню та праву границі
ax.spines[["top", "right"]].set_visible(False)


# Змінюємо підписи на осях
ax.set_xticks([a, b], labels=["$a$", "$b$"])
ax.set_yticks([])


plt.show()
