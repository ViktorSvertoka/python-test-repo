import time


from scipy.optimize import linprog


start = time.time()


c = [1, 2]  # Цільова функція — на мінімум
A_ub = [
    [-2, 1],
    [1, -3],
    [-1, -1],
    [1, 2],
    [-1, 0],
    [0, -1],
]  # Коефіцієнти при нерівностях
b_ub = [0, 0, -1, 5, 0, 0]  # Результати при нерівностях


print(linprog(c, A_ub, b_ub))  # Оптимізація


stop = time.time()
print("Час :")
print(stop - start)
