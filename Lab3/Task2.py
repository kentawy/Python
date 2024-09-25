# Введення двох слів
word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

# Створення множин для кожного слова
set1 = set(word1)
set2 = set(word2)

# Знаходимо літери, які є лише в одному з слів
unique_letters = (set1.symmetric_difference(set2))

# Виведення результату
print(f"Літери, які є тільки в одному зі слів: {', '.join(unique_letters)}")
