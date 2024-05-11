from dataclasses import dataclass


@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height


rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Площа прямокутника 1: {rect1.area()}")
print(f"Площа прямокутника 2: {rect2.area()}")
print(f"Площа прямокутника 3: {rect3.area()}")


# -------------------------------------------------------


from enum import Enum


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


today = Day.MONDAY
print(today)  # Виведе: Day.MONDAY


if today == Day.MONDAY:
    print("Сьогодні понеділок.")
else:
    print("Сьогодні не понеділок.")


print(today.name)
print(today.value)


day_from_value = Day(1)
print(day_from_value)  # Виведе: Day.MONDAY


# -------------------------------------------------------


from enum import Enum, auto


class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELED = auto()


class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")


order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)
order3 = Order("Таро", OrderStatus.NEW)

order1.display_status()
order2.display_status()
order3.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)
order3.update_status(OrderStatus.CANCELED)

order1.display_status()
order2.display_status()
order3.display_status()
