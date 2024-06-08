import numpy as np
import matplotlib.pyplot as plt


# Функція для побудови графіка періодичної функції
def plot_periodic_function(func, period, title):
    x_values = np.linspace(0, 3 * period, 1000)
    y_values = func(x_values)

    plt.plot(x_values, y_values)
    plt.title(title)
    plt.legend()


# Приклад 1: Синус
plt.subplot(2, 2, 1)
plot_periodic_function(np.sin, 2 * np.pi, "Синус")


# Приклад 2: Косинус
plt.subplot(2, 2, 2)
plot_periodic_function(np.cos, 2 * np.pi, "Косинус")


# Приклад 3: Тангенс
plt.subplot(2, 2, 3)
plot_periodic_function(np.tan, np.pi, "Тангенс")


plt.tight_layout()
plt.show()
