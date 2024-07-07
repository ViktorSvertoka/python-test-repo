import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
G = nx.Graph()

# Додаємо вершини
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Додаємо з'єднання
G.add_edge("A", "B")
G.add_edge("B", "C")

# Задаємо розташування вершин
positions = {"A": (0, 0.5), "B": (1, 0.5), "C": (2, 0.5)}

# Малюємо граф
plt.figure(figsize=(6, 6))
nx.draw_networkx(
    G,
    pos=positions,
    with_labels=True,
    font_weight="bold",
    node_color="lightblue",
    edge_color="gray",
)
plt.axis("off")
plt.show()
