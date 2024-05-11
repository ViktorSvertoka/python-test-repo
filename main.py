from collections import UserDict


class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value


# Створення екземпляра власного класу
my_dict = MyDictionary({"a": 1, "b": 2})
my_dict.add_key("c", 3)
my_dict.add_key("d", 4)
my_dict.add_key("e", 5)
print(my_dict)

# -------------------------------------------

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    },
]


class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"


if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("------------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("------------------------------")

    for customer in customers:
        print(customer.email_info())


# -------------------------------------------


from collections import UserList


class MyList(UserList):
    # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)


# Створення екземпляру MyList
my_list = MyList([1, 2, 3])
print("Оригінальний список:", my_list)

# Додавання елементу, якщо він не існує
my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
print("Оновлений список:", my_list)


# -------------------------------------------


class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


countable = CountableList([1, "2", 3, "4"])
countable.append("5")
print(countable.sum())


# -------------------------------------------


from collections import UserString


# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]


# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string)
print("Чи є паліндромом?", my_string.is_palindrome())

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string)
print("Чи є паліндромом?", another_string.is_palindrome())


# -------------------------------------------


class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[: self.MAX_LEN]


ts = TruncatedString("hello world!")
ts.truncate()
print(ts)
