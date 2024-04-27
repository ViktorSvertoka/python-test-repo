from pathlib import Path

path = Path("./picture")

# Перевірка існування
if path.exists():
    print(f"{path} існує")

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")
