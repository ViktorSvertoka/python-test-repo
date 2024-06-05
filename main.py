import plotly.graph_objects as go
import numpy as np


# Генерація точок
num_points = 10
points_x = np.random.rand(num_points) * 10
points_y = np.random.rand(num_points) * 10
points_z = np.random.rand(num_points) * 10


# Створення об'єкта "Figure" для 3D графіка
fig = go.Figure()


# Додавання точок у 3D простір
fig.add_trace(go.Scatter3d(
    x=points_x,
    y=points_y,
    z=points_z,
    mode='markers',
    marker=dict(
        size=5,
        color='blue',  # Колір точок
        opacity=0.8
    ),
    name='Random Points'
))


# Налаштування вигляду графіка
fig.update_layout(
    scene=dict(
        xaxis=dict(title='Вісь X'),
        yaxis=dict(title='Вісь Y'),
        zaxis=dict(title='Вісь Z')
    ),
    title='3D простір з точками',
)


# Відображення графіка
fig.show()

