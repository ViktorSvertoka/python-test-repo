import itertools

val = [1, 2, 3, 4]
perm_set = itertools.permutations(val, 2)
n = 0
for elem in perm_set:
    print(elem)
    n += 1
print(n)
