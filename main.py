import random


def coin_toss():
    # Генеруємо випадкове число (0 або 1) для симуляції підкидання монети
    result = random.randint(0, 1)

    # Визначаємо результат: орел чи решка
    if result == 0:
        return "Орел"
    else:
        return "Решка"


def simulate_coin_tosses(num_tosses):
    # Здійснюємо симуляцію та виводимо результат
    heads_count = 0  # кількість орлів
    tails_count = 0  # кількість решок

    for _ in range(num_tosses):
        toss_result = coin_toss()
        print(toss_result)

        # Підрахунок кількості орлів та решок
        if toss_result == "Орел":
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count


# Введення кількості підкидань
num_tosses = int(input("Введіть кількість підкидань монети: "))

# Запуск симуляції
heads_count, tails_count = simulate_coin_tosses(num_tosses)

# Виведення статистики
print("\nСтатистика:")
print(f"Кількість орлів: {heads_count}")
print(f"Кількість решок: {tails_count}")
print(f"Відносна частота орла: {heads_count / num_tosses:.2f}")
print(f"Відносна частота решки: {tails_count / num_tosses:.2f}")
