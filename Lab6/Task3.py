def analyze_text(text):
    """
    Функція для аналізу тексту та визначення літер.
    """
    # Приводимо текст до нижнього регістру для уніфікації
    text = text.lower()

    # Створюємо множину для всіх літер та словник для їх підрахунку
    letter_count = {}

    for char in text:
        if char.isalpha():  # Перевіряємо, чи символ є літерою
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Визначаємо літери, що зустрічаються не менше двох разів
    letters_two_or_more = {char for char, count in letter_count.items() if count >= 2}

    # Визначаємо літери, що зустрічаються один раз
    letters_one = {char for char, count in letter_count.items() if count == 1}

    return letters_two_or_more, letters_one


def main():
    # Введення тексту користувачем
    text = input("Введіть текст: ")

    # Викликаємо функцію для аналізу тексту
    letters_two_or_more, letters_one = analyze_text(text)

    # Виводимо результати
    print(f"Літери, які входять в текст не менше двох разів: {letters_two_or_more}")
    print(f"Літери, які входять в текст по одному разу: {letters_one}")


if __name__ == "__main__":
    main()
