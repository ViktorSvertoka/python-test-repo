import numpy as np
import matplotlib.pyplot as plt
import random


N = 1000  # розмір вибірки
X = []  # Пустий масив для наповнення


# Цикл з 1000 ітерацій, на кожній з яких додаємо 1 випадковий елемент з нормальним розподілом, із середнім 10 та стандартним відхиленням 5
for i in range(N):
    X.append(random.expovariate(1 / 20))


# формується 2 масиви: n - кількість елементів, що потрапили в інтервал, x - масив границь інтервалів
print(np.histogram(X, bins=10))
n, x = np.histogram(X, bins=10)


# масив початків інтервалів (прибрали останнє, найбільше значення)
xmin = x[:-1]


# ширина інтервалу (різниця двох послідовних стовпчиків).
dx = x[1] - x[0]


# емпірична приведена частота: частка від кількості елементів в інтервалі та загальної кількості елементів
y = n / N


# масив центрів інтервалів
xmid = xmin + dx / 2
# виводимо емпіричну гістограму приведених частот
plt.bar(xmid, y, width=dx, color="y")


# Виводимо підписи на осях
plt.xlabel("x")
plt.ylabel("Частота (ймовірність)")


# Малюємо сітку та гістограму
plt.grid()
plt.show()

(
    array([538, 257, 105, 52, 25, 11, 5, 3, 2, 2]),
    array(
        [
            2.79399809e-02,
            1.59551019e01,
            3.18822639e01,
            4.78094258e01,
            6.37365878e01,
            7.96637497e01,
            9.55909116e01,
            1.11518074e02,
            1.27445236e02,
            1.43372397e02,
            1.59299559e02,
        ]
    ),
)
