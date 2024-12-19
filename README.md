# Python

> [!NOTE]
>
> 1

> [!TIP]
>
> 2

> [!IMPORTANT]
>
> 3

> [!WARNING]
>
> 4

> [!CAUTION]
>
> 5

### Перерахуємо основні правила застосування операцій у порядку їх пріоритету:

1. **Дужки** (): Вирази всередині дужок мають найвищий пріоритет і виконуються
   першими. Дужки можуть бути використані для зміни звичайного порядку
   виконання.
2. **Піднесення до степеня** `**`: Наступним виконується піднесення до степеня.
3. **Унарні плюс `+` та мінус `-`**. Далі йдуть операції унарного плюса та
   мінуса (наприклад, -5 або +3).
4. **Множення `*`, ділення `/`, цілочисельне ділення `//`, остача від ділення
   `%`\*\***: Ці операції мають однаковий пріоритет і виконуються після унарних
   операцій.
5. **Додавання `+` та віднімання `-`**. Виконуються після операцій множення та
   ділення.
6. **Операції порівняння** `==`, `!=`, `>`, `<`, `>=`, `<=`: Виконуються після
   арифметичних операцій.
7. **Логічні операції `not`, `and`, `or`**: В кінці виконуються логічні
   операції, де not має вищий пріоритет, ніж and, який, у свою чергу, має вищий
   пріоритет, ніж or.

### Іменування в Python.

- snake_case - змінні, функції, методи, модулі.
- PascalCase - класи.
- my-package - пакети.
- DB_PASSWORD - константи.

`python3 -m venv .venv`

`source .venv/bin/activate`

`python3 main.py`
