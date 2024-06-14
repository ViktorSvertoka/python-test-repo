import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats


N = len(value_data.Q106)  # розмір вибірки
X = value_data.Q106


# формується 2 масиви: n - кількість елементів, що попали в інтервал, x - масив меж інтервалів
print(np.histogram(X, bins=13))
n, x = np.histogram(X, bins=13)


mean, std = stats.norm.fit(X)


# масив початків інтервалів (прибрали останнє, найбільше значення)
xmin = x[:-1]


# ширина інтервалу (різниця двох послідовних стовпчиків).
dx = x[1] - x[0]


# емпірична приведена частота: частка від кількості елементів в інтервалі та загальної кількості елементів.
y = n / N


# масив центрів інтервалів
xmid = xmin + dx / 2
# виводимо емпіричну гістограму приведених частот
plt.bar(xmid, y, width=dx, color="y")


X1 = np.linspace(-2, 10, 1000)
dist2 = stats.norm(loc=mean, scale=std)
plt.plot(X1, dist2.pdf(X1), "k-")


# Виводимо підписи на осях
plt.xlabel("x")
plt.ylabel("Частота (ймовірність)")


# Малюємо сітку та гістограму.
plt.grid()
plt.show()
