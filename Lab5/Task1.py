def get_integer(prompt):
    """
    Функція для введення цілого числа з перевіркою коректності вводу.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Будь ласка, введіть ціле число.")


def get_array(n):
    """
    Функція для введення масиву з n цілих чисел від користувача.
    """
    array = []
    print(f"Введіть {n} цілих чисел:")
    while len(array) < n:
        try:
            # Можна вводити всі числа через пробіл за один раз
            elements = input().split()
            for elem in elements:
                if len(array) < n:
                    array.append(int(elem))
                else:
                    break
        except ValueError:
            print("Будь ласка, вводьте тільки цілі числа.")
    return array


def find_minimum(array):
    """
    Функція для знаходження мінімального елемента в масиві.
    """
    if not array:
        return None
    minimum = array[0]
    for num in array:
        if num < minimum:
            minimum = num
    return minimum


def main():
    print("Знайдення мінімального елемента в масиві.")

    # Ввід довжини масиву
    n = get_integer("Введіть довжину масиву (N): ")
    if n <= 0:
        print("Довжина масиву повинна бути позитивним числом.")
        return

    # Ввід масиву
    array = get_array(n)
    print(f"Введений масив: {array}")

    # Пошук мінімального елемента
    minimum = find_minimum(array)
    if minimum is not None:
        print(f"Мінімальний елемент масиву: {minimum}")
    else:
        print("Масив порожній.")


if __name__ == "__main__":
    main()
