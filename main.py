# Створення стеку
def create_stack():
    return []


# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0


# Додавання елементу
def push(stack, item):
    stack.append(item)


# Вилучення елементу
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")


# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")


stack = create_stack()
push(stack, "a")
push(stack, "b")
push(stack, "c")


print(peek(stack))  # Виведе 'c'
print(pop(stack))  # Виведе 'c'


from collections import deque

# Створення черги
queue = deque()

# Enqueue: Додавання елементів
queue.append("a")
queue.append("b")
queue.append("c")

print("Черга після додавання елементів:", list(queue))

# Dequeue: Видалення елемента
print("Видалений елемент:", queue.popleft())

print("Черга після видалення елемента:", list(queue))

# Peek: Перегляд першого елемента
print("Перший елемент у черзі:", queue[0])

# IsEmpty: Перевірка на порожнечу
print("Чи черга порожня:", len(queue) == 0)

# Size: Розмір черги
print("Розмір черги:", len(queue))


from collections import deque

# Створення пустої двосторонньої черги
d = deque()

# Додаємо елементи в чергу
d.append("middle")  # Додаємо 'middle' в кінець черги
d.append("last")  # Додаємо 'last' в кінець черги
d.appendleft("first")  # Додаємо 'first' на початок черги

# Виведення поточного стану черги
print("Черга після додавання елементів:", list(d))

# Видалення та виведення останнього елемента (з правого кінця)
print("Видалений останній елемент:", d.pop())

# Видалення та виведення першого елемента (з лівого кінця)
print("Видалений перший елемент:", d.popleft())

# Виведення поточного стану черги після видалення елементів
print("Черга після видалення елементів:", list(d))
