my_dict = {}
my_dict["key1"] = "value1"
my_dict["key2"] = "value2"
print(my_dict)  # {'key1': 'value1', 'key2': 'value2'}


del my_dict["key1"]
print(my_dict)  # {'key2': 'value2'}


value = my_dict.get("key2")
print(value)  # value2


my_dict["key2"] = "new value"
print(my_dict)  # {'key2': 'new value'}


key1 = "example"
hash_value1 = hash(key1)
print(hash_value1)  # -4049593035154628903

key2 = "another example"
hash_value2 = hash(key2)
print(hash_value2)  # 5109324920784817575


import hashlib

data = "example data"

# Використання SHA-256
hashed_data = hashlib.sha256(data.encode())
print(
    hashed_data.hexdigest()
)  # 44752f37272e944fd2c913a35342eaccdd1aaf189bae50676b301ab213fc5061


import hashlib
import os


def get_hash(path):
    """Повертає хеш-значення для файлу."""
    with open(path, "rb") as file:
        bytes = file.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        return readable_hash


def find_duplicates(directory):
    """Шукає дублікати в директорії."""
    hashes = {}
    duplicates = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            file_hash = get_hash(path)
            if file_hash not in hashes:
                hashes[file_hash] = path
            else:
                duplicates.append((path, hashes[file_hash]))
    return duplicates


# Пошук дублікатів у заданій директорії
duplicates = find_duplicates("/path/to/directory")
for duplicate in duplicates:
    print(f"Дублікатні файли: {duplicate[0]} та {duplicate[1]}")
