import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams.update({"font.size": 12})


x = np.linspace(0, 10, 100)
x1 = []
for i in range(100):
    x1.append(3)
y1 = np.linspace(0, 10, 100)
f1 = 2 * x
f2 = (1 / 4) * x
f3 = 1 - x


# вказуємо в аргументі label текст легенди
plt.plot(x, f1, ":b", label="x2>2x1")
plt.plot(x, f2, "--b", label="x2<1/4x1")
plt.plot(x, f3, "y", label="x2>1-x1")


plt.xlabel(r"$x2$", fontsize=16)
plt.ylabel(r"$x3$", fontsize=16)


plt.xlim([0, 2])
plt.ylim([0, 2])


# виводимо легенду
plt.legend(fontsize=14)


plt.tight_layout()
plt.show()
