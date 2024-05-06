add = lambda x, y: x + y
print(add(5, 3))  # Виведе 8


nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)


numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x**2, numbers):
    print(i)


numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x**2, numbers))
print(squared_nums)


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)

print(list(sum_nums))


numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x**2, numbers))
print(squared_nums)


nums = [1, 2, 3, 4, 5]
squared_nums = [x * x for x in nums]
print(squared_nums)


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)
