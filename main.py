byte_array = bytearray(b"Kill Bill")
byte_array[0] = ord("B")
byte_array[5] = ord("K")
print(byte_array)


string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")


text = "Python Programming"
print(text.casefold())


german_word = "straße"  # В нижньому регістрі
search_word = "STRASSE"  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")
