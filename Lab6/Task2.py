def find_top_five_max(lst):
    """
    Функція для знаходження перших п'яти максимальних елементів списку.
    """
    # Перевірка, чи достатньо елементів у списку
    if len(lst) < 5:
        print("У списку недостатньо елементів для виконання операції.")
        return lst

    # Сортуємо список у зворотному порядку та беремо перші п'ять
    top_five = sorted(lst, reverse=True)[:5]

    return top_five


def main():
    # Введення списку користувачем
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = list(map(int, user_input.split()))  # перетворюємо введені дані на список цілих чисел

    print(f"Введений список: {lst}")

    # Викликаємо функцію для пошуку максимальних елементів
    top_five_max = find_top_five_max(lst)

    print(f"Перші п'ять максимальних елементів: {top_five_max}")


if __name__ == "__main__":
    main()