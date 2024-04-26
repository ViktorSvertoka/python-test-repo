from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path("example.txt")

# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text)


from pathlib import Path

# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")

# Бінарні дані для запису
data = b"Python is great!"

# Запис байтів у файл
file_path.write_bytes(data)


from pathlib import Path

# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")

# Читання байтів з файлу
binary_data = file_path.read_bytes()
print(binary_data)
