# Введення речення
sentence = input("Введіть речення: ")

# Розбиваємо речення на слова
words = sentence.split()

# Знаходимо слова, що починаються і закінчуються на ту саму літеру
matching_words = [word for word in words if word[0].lower() == word[-1].lower()]

# Виводимо результат
if matching_words:
    print(f"Слова, що починаються і закінчуються на одну й ту ж літеру: {', '.join(matching_words)}")
else:
    print("Немає слів, що починаються і закінчуються на одну й ту ж літеру.")
