import matplotlib.pyplot as plt

# Дані: прізвища та кількість осіб
data = [
    {"surname": "Іванов", "phone": "380501234567"},
    {"surname": "Петров", "phone": "380502345678"},
    {"surname": "Сидоров", "phone": "380503456789"},
    {"surname": "Коваленко", "phone": "380504567890"},
    {"surname": "Бондаренко", "phone": "380505678901"},
    {"surname": "Ткаченко", "phone": "380506789012"},
    {"surname": "Шевченко", "phone": "380507890123"},
    {"surname": "Кравченко", "phone": "380508901234"},
    {"surname": "Мельник", "phone": "380509012345"},
    {"surname": "Гнатюк", "phone": "380510123456"},
]

# Кількість осіб
total_people = len(data)

# Відсоток для кожного прізвища
labels = [entry['surname'] for entry in data]
sizes = [1] * total_people  # Кожен прізвище представляє однакову частину

# Створення кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Додавання заголовка
plt.title("Відсотковий розподіл прізвищ")

# Відображення діаграми
plt.axis('equal')  # Зробити діаграму круглою
plt.show()
