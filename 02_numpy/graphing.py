import matplotlib.pyplot as plt
import numpy as np
# IF NOT INSTALLED `pip install numpy`
# `pip install matplotlib`

# basic line
x_values = np.arange(20)  # 0, 1, 2, 3, 4
# y_values = x_values * 2  # 0, 2, 4, 6, 8
y_values = x_values * x_values  # 0, 2, 4, 6, 8

fig, ax = plt.subplots()


random_noise = 20 * (np.random.random(x_values.shape) - 0.5)

y_data = y_values + random_noise  # 0, 2, 4, 6, 8

ax.scatter(x_values, y_values, color=(1, 0, 0), marker="x", label="ground_truth")
ax.scatter(x_values, y_data, color=(0, 0, 1), marker="o", label="data")

coeffs = np.polyfit(x_values, y_data, deg=1)

print("coeffs", coeffs)
"""
e.g. [2.2, -0.5] => y = 2.2*x^1 + (-0.5)
    [5, 3, 2] => y = 5*x^2 + 3*x + 2
"""

pred_y = x_values*coeffs[0] + coeffs[1]

ax.plot(x_values, pred_y, c=(0, 1, 0), label="predicted_value")

ax.legend()
plt.show()


