with open("raw_data.bin", "wb") as fh:
    fh.write(b"Hello world!")


s = b"Hello!"
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')


byte_str = "some text".encode()
print(byte_str)


# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел


for num in [127, 255, 156]:
    print(hex(num))


print(ord("a"))


print(chr(128))


s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)


print(b"Hello world!".decode("utf-16"))


# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
