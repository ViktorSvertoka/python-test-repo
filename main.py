import itertools

val = [1, 2, 3, 4]
perm_set = itertools.permutations(val, 2)
n = 0
for elem in perm_set:
    print(elem)
    n += 1
print(n)


import itertools

val = [1, 2, 3, 4]
perm_set = itertools.permutations(val)
n = 0
for elem in perm_set:
    print(elem)
    n += 1
print(n)


import itertools

val = [1, 2, 3, 4]
com_set = itertools.combinations(val, 2)
n = 0
for elem in com_set:
    print(elem)
    n += 1
print(n)
