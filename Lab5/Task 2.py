def fill_array(n):
    """
    Функція для заповнення двовимірного масиву розміром n x n відповідно до зразка.
    """
    array = [[0 for _ in range(n)] for _ in range(n)]

    # Заповнення масиву відповідно до правила
    for i in range(n):
        for j in range(i, n):
            array[i][j] = j - i + 1

    return array


def print_array(array):
    """
    Функція для виведення двовимірного масиву у вигляді матриці.
    """
    for row in array:
        print(" ".join(map(str, row)))


def main():
    n = 7  # Розмір масиву 7x7
    array = fill_array(n)
    print("Заповнений масив:")
    print_array(array)


if __name__ == "__main__":
    main()
