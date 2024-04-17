num = int(input("Введіть число: "))

length = len(str(num))

if length == 2 and num % 2 == 0:
    print("Парне двозначне число")
else:
    print("Ні")
