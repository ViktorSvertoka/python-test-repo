fh = open("text.txt", "w")
try:
    # Виконання операцій з файлом
    fh.write("Some data")
finally:
    # Закриття файлу в блоку finally гарантує, що файл закриється навіть у разі помилки
    fh.close()


with open("text.txt", "w") as fh:
    # Виконання операцій з файлом
    fh.write("Some data")
# Файл автоматично закриється після виходу з блоку with


with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)
