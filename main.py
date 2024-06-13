import math

x = [113, 114, 106, 108, 120, 104, 116, 112, 110, 118, 103, 120]
y = [10, 15, 20, 15, 24, 11, 20, 20, 18, 24, 14, 27]


# Обраховуємо суму та середнє значення
sum_x = sum(x)
avg_x = sum(x) / len(x)
sum_y = sum(y)
avg_y = sum(y) / len(y)


# Обраховуємо ряд, який є різницею між первинним рядом та середнім значенням ряду
x_minus_avg = []
y_minus_avg = []
for i in range(len(x)):
    x_minus_avg.append(x[i] - avg_x)
    y_minus_avg.append(y[i] - avg_y)


# Обраховуємо квадрати різниці значень ряду та її середніх, і добуток різниць значень ряду та їх середніх різних змінних
xma2 = []
yma2 = []
xma_yma = []
for i in range(len(x_minus_avg)):
    xma2.append(x_minus_avg[i] ** 2)
    yma2.append(y_minus_avg[i] ** 2)
    xma_yma.append(x_minus_avg[i] * y_minus_avg[i])


# Обраховуємо суми отриманих рядів
sum_xma2 = sum(xma2)
sum_yma2 = sum(yma2)
sum_xma_yma = sum(xma_yma)


# Обраховуємо критерій кореляції Пірсона
r_x_y = sum_xma_yma / (math.sqrt(sum_xma2 * sum_yma2))
print(r_x_y)
