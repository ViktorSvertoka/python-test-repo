import itertools

val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
com_set = itertools.combinations(val, 5)
n = 0
for elem in com_set:
    # print(elem)
    n += 1
C59 = n
print(C59)
val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
com_set = itertools.combinations(val, 6)
n = 0
for elem in com_set:
    # print(elem)
    n += 1
C610 = n
print(C610)
P = C59 / C610
print(P)


import itertools

val = [1, 2, 3, 4, 5, 6, 7, 8]
com_set = itertools.combinations(val, 4)
n = 0
for elem in com_set:
    # print(elem)
    n += 1
C48 = n
print(C48)
val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
com_set = itertools.combinations(val, 6)
n = 0
for elem in com_set:
    # print(elem)
    n += 1
C610 = n
print(C610)
P = C48 / C610
print(P)
