def remove_elements(lst):
    """
    Функція для видалення другого і передостаннього елемента зі списку.
    """
    if len(lst) < 2:
        print("Список занадто короткий для виконання операції.")
        return lst

    # Видалення другого елемента
    del lst[1]

    # Видалення передостаннього елемента
    if len(lst) > 1:
        del lst[-2]

    return lst


def main():
    # Введення списку користувачем
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split()  # перетворюємо введені дані на список рядків

    print(f"Введений список: {lst}")

    # Викликаємо функцію для видалення елементів
    updated_list = remove_elements(lst)

    print(f"Список після видалення другого і передостаннього елемента: {updated_list}")


if __name__ == "__main__":
    main()
