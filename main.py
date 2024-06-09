import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz


X = np.linspace(0, 7)
Y = (X - 3) * (X - 5) * (X - 7) + 85  # функція
plt.plot(X, Y, "k-", label="Функція")


Y1 = np.diff(Y) / np.diff(X)  # похідна
plt.plot(X[:-1], Y1, "k--", label="Похідна")
Y1 = np.gradient(Y, X[1] - X[0])  # або
plt.plot(X, Y1, "k--")


Y_int = cumtrapz(Y, X, initial=0)  # первісна
plt.plot(X, Y_int, "k:", label="Первісна")
plt.xlabel("$x$")
plt.ylabel("$y$")
legend = plt.legend(loc="upper center", shadow=True, fontsize="x-large")
plt.grid()
plt.show()


# Запускаємо малювання графіка
plt.show()
