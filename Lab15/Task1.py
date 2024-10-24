import pandas as pd

# Створення телефонного довідника (або завантаження з JSON)
phonebook = {
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

# Перетворення словника на DataFrame
df = pd.DataFrame(list(phonebook.items()), columns=['Surname', 'Phone'])

# Додавання нових даних (як приклад)
additional_data = {
    "Дорошенко": "380511234567",
    "Горбачов": "380512345678",
    "Лебедєв": "380513456789"
}

# Створення DataFrame з новими даними
additional_df = pd.DataFrame(list(additional_data.items()), columns=['Surname', 'Phone'])

# Використання concat для додавання нових записів
df = pd.concat([df, additional_df], ignore_index=True)

# Виведення DataFrame на екран
print("Телефонний довідник у форматі DataFrame:")
print(df)

# Припустимо, ми можемо виконати агрегацію за початковими цифрами телефонних номерів
df['Phone Prefix'] = df['Phone'].str[:5]  # Витягуємо перші 5 цифр номера

# Виконання групування за префіксами номерів
grouped = df.groupby('Phone Prefix').size().reset_index(name='Count')

# Виведення результату групування
print("\nГрупування за префіксами номерів:")
print(grouped)

# Аггрегація (наприклад, кількість записів на кожний префікс)
aggregation = df.groupby('Phone Prefix').agg({'Surname': 'count'}).reset_index()

print("\nАгрегація за кількістю записів на кожен префікс:")
print(aggregation)
