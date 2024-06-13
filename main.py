import numpy as np
import statistics as st
import math

x1 = [6, 7, 4, 5, 4, 5, 3, 6, 7, 3, 7, 3, 5, 4, 4, 3, 5, 4]
x2 = [4, 4, 5, 4, 1, 5, 5, 3, 3, 6, 2, 3, 4, 3, 7, 5, 3, 2, 4, 5]


x1_avg = np.average(x1)
x2_avg = np.average(x2)


x1_disp = st.variance(x1)
x2_disp = st.variance(x2)


n1 = len(x1)
n2 = len(x2)


print(f"Середні значення: {x1_avg} {x2_avg}")
print(f"Дисперсії: {x1_disp} {x2_disp}")
print(f"Розмір вибірки: {n1} {n2}")


t = (x1_avg - x2_avg) / (
    math.sqrt(
        (((n1 - 1) * x1_disp + (n2 - 1) * x2_disp)) / (n1 + n2 - 2) * (1 / n1 + 1 / n2)
    )
)
print(t)
# t критичне для 38 ступенів свободи 2,024
# Визначаємо дисперсію
