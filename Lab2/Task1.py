# Task1.py

import math
from mod import calculate_amebas  # Імпортуємо функцію з модуля

# Функція для обчислення z
def calculate_z(alpha):
    return (math.sqrt(2) / 2) * math.sin(alpha / 2)

# Основна функція програми
def main():
    # Завдання 1: Обчислення z
    try:
        alpha = float(input("Введіть значення α для обчислення z: "))
        z = calculate_z(alpha)
        print(f"Значення z: {z}")
    except ValueError:
        print("Будь ласка, введіть коректне число для α.")

    # Завдання 2: Використання функції з модуля
    try:
        n = int(input("Введіть кількість годин n для обчислення кількості амеб: "))
        amebas = calculate_amebas(n)  # Викликаємо функцію з модуля
        print(f"Кількість амеб через {n} годин: {amebas}")
    except ValueError:
        print("Будь ласка, введіть коректне ціле число для n.")

# Запуск програми
if __name__ == "__main__":
    main()
