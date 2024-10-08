# Функція для обчислення X на основі заданих умов
def calculate_x(a, b):
    if a > b:
        return (a / b) - 1
    elif a == b:
        return -25
    elif a < b:
        return (a ** 3 - 5) / a


# Основна функція для отримання та перевірки вхідних даних
def main():
    # Цикл перевірки вхідних даних
    while True:
        try:
            a = float(input("Введіть додатне значення для a: "))
            b = float(input("Введіть додатне значення для b: "))
            if a > 0 and b > 0:
                break
            else:
                print("І a, і b повинні бути додатними числами. Спробуйте ще раз.")
        except ValueError:
            print("Неправильно введено. Будь ласка, введіть числові значення.")

    # Обчислення та виведення результату
    x = calculate_x(a, b)
    print(f"Значення X дорівнює: {x}")


# Запуск програми
main()
