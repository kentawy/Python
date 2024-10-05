import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def Y(x):
    return 15 * np.sin(10 * x) * np.cos(3 * x)

# Генерація значень x
x_values = np.linspace(-3, 3, 400)
y_values = Y(x_values)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Y(x) = 15*sin(10x)*cos(3x)', color='b')
plt.title('Графік функції Y(x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
