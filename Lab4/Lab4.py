text = "Пайтон є однією з найпопулярніших мов програмування у світі. Завдяки простому синтаксису та широким можливостям, він використовується для розробки веб-додатків, аналізу даних, автоматизації та багатьох інших завдань. Крім того, його легко вивчати як початківцям, так і досвідченим програмістам. Спільнота Пайтон надає багато бібліотек та інструментів, які спрощують роботу над проектами будь-якої складності. Завдяки цьому, мова стає універсальним інструментом для вирішення різноманітних проблем, що виникають у процесі розробки."

# Функції Дмитренко Богдан: lower(), replace(), count()
# Приводимо текст до нижнього регістру
text_lower = text.lower()
print("Текст у нижньому регістрі:", text_lower)

# Замінюємо слово 'Пайтон' на 'Ця мова'
text_replaced = text_lower.replace("пайтон", "ця мова")
print("Замінений текст:", text_replaced)

# Рахуємо кількість входжень слова 'мова'
language_count = text_replaced.count("мова")
print("Кількість входжень слова 'мова':", language_count)

# Функції Рубан Богдан: split(), join(), find()
# Розбиваємо текст на слова
words = text_replaced.split()
print("Список слів:", words)

# З'єднуємо слова в рядок через дефіс
joined_text = '-'.join(words)
print("Текст, з'єднаний через дефіс:", joined_text)

# Знаходимо індекс першого входження слова 'мова'
index_language = text_replaced.find("мова")
print("Індекс першого входження слова 'мова':", index_language)

# Функції Лук`янченко Сергій: capitalize(), endswith(), startswith()
# Капіталізуємо перше слово в рядку
capitalized_text = text_replaced.capitalize()
print("Капіталізований текст:", capitalized_text)

# Перевіряємо, чи закінчується рядок на слово 'розробки.'
ends_with_learning = text_replaced.endswith("розробки.")
print("Закінчується на 'навчанні.':", ends_with_learning)

# Перевіряємо, чи починається рядок з 'пайтон'
starts_with_python = text_replaced.startswith("пайтон")
print("Починається з 'пайтон':", starts_with_python)

# Функції Петрушко Ярослав: isalpha(), isdigit(), strip()
# Перевіряємо, чи складається рядок тільки з букв
is_alpha = text_replaced.isalpha()
print("Складається лише з букв:", is_alpha)

# Перевіряємо, чи складається рядок тільки з цифр
is_digit = text_replaced.isdigit()
print("Складається лише з цифр:", is_digit)

# Видаляємо зайві пробіли з початку та кінця рядка
stripped_text = text_replaced.strip()
print("Текст без зайвих пробілів:", stripped_text)

# Функції Гаценко Максим: swapcase(), rfind(), zfill()
# Змінюємо регістр літер: великі стають малими і навпаки
swapped_text = text_replaced.swapcase()
print("Текст зі зміненим регістром:", swapped_text)

# Знаходимо індекс останнього входження слова 'мова'
last_index_language = text_replaced.rfind("мова")
print("Останній індекс входження слова 'мова':", last_index_language)

# Додаємо нулі перед рядком до довжини 50 символів
zero_filled_text = text_replaced.zfill(50)
print("Текст із доданими нулями:", zero_filled_text)
