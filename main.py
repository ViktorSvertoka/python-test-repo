users = [
    {"user_id": 134, "user_name": "Inna"},
    {"user_id": 135, "user_name": "Bob"},
    {"user_id": 136, "user_name": "Alice"},
    {"user_id": 137, "user_name": "Stan"},
]

print(len(users))  # 4
print(users[0]["user_id"])  # 134
print(users[0]["user_name"])  # Inna


my_fruit = "apple"
other_fruit = "banana"
new_fruit = "lime"

all_fruits = [my_fruit, other_fruit, new_fruit]
print(all_fruits)  # ['apple', 'banana', 'lime']


posts_ids = [111, 222, 333, 444]
print(posts_ids[10])  # IndexError: list index out of range
