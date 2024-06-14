import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams.update({"font.size": 12})


x = np.linspace(0, 10, 100)
x1 = []
for i in range(100):
    x1.append(2)
y1 = np.linspace(0, 10, 100)
f1 = (5 / 2) * x + 1
f2 = 3 + 0 * x
f3 = 11 / 2 + x


# вказуємо в аргументі label вміст легенди
plt.plot(x, f1, ":b", label="< (5/2)*x3+1")
plt.plot(x, f2, "--r", label=">3")
plt.plot(x1, y1, "k", label="x3<2")
plt.plot(x, f3, "y", label="<11/2+x3")
# plt.plot(x, f4, 'k', label='total')


plt.xlabel(r"$x2$", fontsize=16)
plt.ylabel(r"$x3$", fontsize=16)


plt.xlim([0, 10])
plt.ylim([0, 10])


# виводимо легенду
plt.legend(fontsize=14)


plt.tight_layout()
plt.show()
