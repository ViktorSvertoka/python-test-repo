import matplotlib.pyplot as plt


n = [0.0016, 0.0272, 0.1808, 0.5904, 1]
print(n)
plt.stairs(n, fill=True, label="Distribution")
plt.grid(True)
plt.show()
