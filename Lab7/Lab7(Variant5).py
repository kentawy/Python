import json
import os

# Файл для збереження телефонного довідника
PHONEBOOK_FILE = 'phonebook.json'


def load_phonebook():
    """Завантажує телефонний довідник з файлу, якщо він існує."""
    if os.path.exists(PHONEBOOK_FILE):
        try:
            with open(PHONEBOOK_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Помилка формату файлу. Створюється новий телефонний довідник.")
    # Якщо файл не існує або виникла помилка, створюємо початковий довідник
    return {
        "Іванов": "380501234567",
        "Петров": "380502345678",
        "Сидоров": "380503456789",
        "Коваленко": "380504567890",
        "Бондаренко": "380505678901",
        "Ткаченко": "380506789012",
        "Шевченко": "380507890123",
        "Кравченко": "380508901234",
        "Мельник": "380509012345",
        "Гнатюк": "380510123456"
    }


def save_phonebook(phonebook):
    """Зберігає телефонний довідник у файл."""
    try:
        with open(PHONEBOOK_FILE, 'w', encoding='utf-8') as file:
            json.dump(phonebook, file, ensure_ascii=False, indent=4)
        print("Телефонний довідник успішно збережено.")
    except Exception as e:
        print(f"Сталася помилка при збереженні довідника: {e}")


def display_all_entries(phonebook):
    """Виводить всі записи телефонного довідника."""
    if not phonebook:
        print("Телефонний довідник порожній.")
        return
    print("\nВсі записи телефонного довідника:")
    for surname, phone in phonebook.items():
        print(f"Прізвище: {surname}, Телефон: {phone}")


def add_entry(phonebook):
    """Додає новий запис до телефонного довідника."""
    surname = input("Введіть прізвище: ").strip()
    phone = input("Введіть номер телефону: ").strip()
    if surname in phonebook:
        print("Ця особа вже існує у телефонному довіднику.")
    else:
        phonebook[surname] = phone
        print("Запис успішно додано.")
        save_phonebook(phonebook)


def remove_entry(phonebook):
    """Видаляє запис з телефонного довідника за прізвищем."""
    surname = input("Введіть прізвище для видалення: ").strip()
    try:
        del phonebook[surname]
        print(f"Запис для {surname} успішно видалено.")
        save_phonebook(phonebook)
    except KeyError:
        print(f"Запис для {surname} не знайдено.")


def view_sorted_entries(phonebook):
    """Виводить записи телефонного довідника, відсортовані за прізвищем."""
    if not phonebook:
        print("Телефонний довідник порожній.")
        return
    sorted_surnames = sorted(phonebook.keys())
    print("\nТелефонний довідник (відсортовано за прізвищем):")
    for surname in sorted_surnames:
        print(f"Прізвище: {surname}, Телефон: {phonebook[surname]}")


def find_phone_by_surname(phonebook):
    """Знаходить номер телефону за прізвищем."""
    surname = input("Введіть прізвище для пошуку телефону: ").strip()
    phone = phonebook.get(surname)
    if phone:
        print(f"Телефон {surname}: {phone}")
    else:
        print(f"Запис для {surname} не знайдено.")


def find_surname_by_phone(phonebook):
    """Знаходить прізвище за номером телефону."""
    phone = input("Введіть номер телефону для пошуку прізвища: ").strip()
    surnames = [surname for surname, p in phonebook.items() if p == phone]
    if surnames:
        print(f"Особи з номером телефону {phone}: {', '.join(surnames)}")
    else:
        print(f"Запис з номером телефону {phone} не знайдено.")


def main():
    phonebook = load_phonebook()

    while True:
        print("\n--- Телефонний довідник ---")
        print("1. Вивести всі записи")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Переглянути записи, відсортовані за прізвищем")
        print("5. Знайти телефон за прізвищем")
        print("6. Знайти прізвище за телефоном")
        print("7. Вихід")

        choice = input("Оберіть опцію (1-7): ").strip()

        if choice == '1':
            display_all_entries(phonebook)
        elif choice == '2':
            add_entry(phonebook)
        elif choice == '3':
            remove_entry(phonebook)
        elif choice == '4':
            view_sorted_entries(phonebook)
        elif choice == '5':
            find_phone_by_surname(phonebook)
        elif choice == '6':
            find_surname_by_phone(phonebook)
        elif choice == '7':
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
