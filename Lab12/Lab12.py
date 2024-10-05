import json

# Файл для зберігання даних
data_file = 'contacts.json'

# Початкові дані (прізвища та номери телефонів)
initial_data = [
    {"surname": "Іванов", "phone": "123456789"},
    {"surname": "Петров", "phone": "987654321"},
    {"surname": "Сидоров", "phone": "555444332"},
    {"surname": "Коваленко", "phone": "333222111"},
    {"surname": "Шевченко", "phone": "777888999"},
    {"surname": "Грищенко", "phone": "666555444"},
    {"surname": "Лисенко", "phone": "444333222"},
    {"surname": "Кравченко", "phone": "222111000"},
    {"surname": "Ткаченко", "phone": "111000999"},
    {"surname": "Мельник", "phone": "999888777"}
]


# Створення початкового JSON файлу
def create_initial_data():
    with open(data_file, 'w') as f:
        json.dump(initial_data, f, ensure_ascii=False, indent=4)


# Виведення вмісту JSON файлу
def display_contacts():
    try:
        with open(data_file, 'r') as f:
            contacts = json.load(f)
            print("Вміст JSON файлу:")
            for contact in contacts:
                print(f"Прізвище: {contact['surname']}, Телефон: {contact['phone']}")
    except FileNotFoundError:
        print("Файл не знайдено. Створіть файл спочатку.")
    except json.JSONDecodeError:
        print("Помилка декодування JSON.")


# Додавання нового запису
def add_contact(surname, phone):
    try:
        with open(data_file, 'r+') as f:
            contacts = json.load(f)
            contacts.append({"surname": surname, "phone": phone})
            f.seek(0)  # Переміщення курсора на початок файлу
            json.dump(contacts, f, ensure_ascii=False, indent=4)
            f.truncate()  # Обрізаємо файл, якщо новий запис коротший
            print(f"Контакт {surname} успішно додано.")
    except FileNotFoundError:
        print("Файл не знайдено. Спочатку створіть файл.")
    except json.JSONDecodeError:
        print("Помилка декодування JSON.")


# Видалення запису
def remove_contact(surname):
    try:
        with open(data_file, 'r+') as f:
            contacts = json.load(f)
            contacts = [contact for contact in contacts if contact["surname"] != surname]
            f.seek(0)
            json.dump(contacts, f, ensure_ascii=False, indent=4)
            f.truncate()
            print(f"Контакт {surname} успішно видалено.")
    except FileNotFoundError:
        print("Файл не знайдено. Спочатку створіть файл.")
    except json.JSONDecodeError:
        print("Помилка декодування JSON.")


# Пошук за прізвищем
def find_by_surname(surname):
    try:
        with open(data_file, 'r') as f:
            contacts = json.load(f)
            for contact in contacts:
                if contact['surname'] == surname:
                    print(f"Телефон для {surname}: {contact['phone']}")
                    return
            print(f"Контакт {surname} не знайдено.")
    except FileNotFoundError:
        print("Файл не знайдено. Спочатку створіть файл.")
    except json.JSONDecodeError:
        print("Помилка декодування JSON.")


# Пошук за номером телефону
def find_by_phone(phone):
    try:
        with open(data_file, 'r') as f:
            contacts = json.load(f)
            for contact in contacts:
                if contact['phone'] == phone:
                    print(f"Прізвище для {phone}: {contact['surname']}")
                    return
            print(f"Контакт з номером {phone} не знайдено.")
    except FileNotFoundError:
        print("Файл не знайдено. Спочатку створіть файл.")
    except json.JSONDecodeError:
        print("Помилка декодування JSON.")


# Основна функція для діалогу з користувачем
def main():
    create_initial_data()  # Створюємо файл з початковими даними
    while True:
        print("\nВиберіть дію:")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Пошук за прізвищем")
        print("5. Пошук за номером телефону")
        print("6. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            display_contacts()
        elif choice == '2':
            surname = input("Введіть прізвище: ")
            phone = input("Введіть номер телефону: ")
            add_contact(surname, phone)
        elif choice == '3':
            surname = input("Введіть прізвище для видалення: ")
            remove_contact(surname)
        elif choice == '4':
            surname = input("Введіть прізвище для пошуку: ")
            find_by_surname(surname)
        elif choice == '5':
            phone = input("Введіть номер телефону для пошуку: ")
            find_by_phone(phone)
        elif choice == '6':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
