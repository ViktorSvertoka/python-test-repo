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

### Активація і робота з віртуальним середовищем в Python.

`python3 -m venv .venv`

`which python`

`source .venv/bin/activate`

`deactivate`

### Виконання коду в Python.

`python3 main.py`

### Popular Python Libraries

| Library            | Description                                                                            | Installation Command         |
| ------------------ | -------------------------------------------------------------------------------------- | ---------------------------- |
| **colorama**       | Adds color support to console output                                                   | `pip install colorama`       |
| **click**          | For creating command-line interfaces with options and prompts                          | `pip install click`          |
| **rich**           | For beautiful and rich text in the terminal, including tables, progress bars, and more | `pip install rich`           |
| **typer**          | For building CLI applications with auto-complete and rich features                     | `pip install typer`          |
| **prompt_toolkit** | Enables interactive command-line input with dropdowns and auto-completion              | `pip install prompt_toolkit` |
| **pyfiglet**       | Renders ASCII art from text in the terminal                                            | `pip install pyfiglet`       |
| **tabulate**       | Formats data as tables for console output                                              | `pip install tabulate`       |
| **inquirer**       | Creates interactive command-line prompts                                               | `pip install inquirer`       |
| **sh**             | Simplifies shell command execution in Python                                           | `pip install sh`             |
| **blessed**        | For advanced terminal control and styling                                              | `pip install blessed`        |
