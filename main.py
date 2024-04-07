int_num = 50
str_val = "abc"

print(str_val * int_num)
print(int_num.__mul__(str_val))
print(str_val.__rmul__(int_num))
