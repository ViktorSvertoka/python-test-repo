even_nums = filter(lambda x: x % 2 == 0, range(1, 21))

print(list(even_nums))


def is_positive(x):
    return x > 0


nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)

print(list(positive_nums))


some_str = "Видавництво А-БА-БА-ГА-ЛА-МА-ГА"

new_str = "".join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)


nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)


some_str = "Видавництво А-БА-БА-ГА-ЛА-МА-ГА"

new_str = "".join([x for x in some_str if x.islower()])
print(new_str)


nums = [0, False, 5, 0]
result = any(nums)
print(result)


nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)
print(result)


nums = [1, 2, 3, 4]
result = all(nums)
print(result)


nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums)
print(is_all_even)


words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)
