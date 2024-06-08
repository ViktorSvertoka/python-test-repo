import matplotlib.pyplot as plt
import numpy as np


# Послідовність, яка збігається до 0
n1 = np.arange(1, 100)
a_n = 1 / n1


# Послідовність збіжна до 1/2
n2 = np.arange(1, 100)
b_n = (n2 + 1) / (2 * n2)


# Збіжна послідовність до e
n3 = np.arange(1, 100)
c_n = (1 + 1 / n3) ** n3


# Невласна геометрична послідовність, що розходиться
n4 = np.arange(1, 100)
d_n = 2**n4


# Візуалізація
plt.figure(figsize=(12, 8))


plt.subplot(2, 2, 1)
plt.plot(n1, a_n, marker="o")
plt.axhline(y=0, color="black", linestyle="--", linewidth=0.8, alpha=0.7)
plt.title(r"$\frac{1}{n}$; Границя: 0")


plt.subplot(2, 2, 2)
plt.plot(n2, b_n, marker="o")
plt.axhline(y=1 / 2, color="black", linestyle="--", linewidth=0.8, alpha=0.7)
plt.title(r"$\frac{n + 1}{2n}$; Границя: $\frac{1}{2}$")


plt.subplot(2, 2, 3)
plt.plot(n3, c_n, marker="o")
plt.axhline(y=np.e, color="black", linestyle="--", linewidth=0.8, alpha=0.7)
plt.title(r"$(1 + \frac{1}{n})^n$; Границя: $e$")


plt.subplot(2, 2, 4)
plt.plot(n4, d_n, marker="o")
plt.title("$2^n$; Розходиться")


plt.tight_layout()
plt.show()
