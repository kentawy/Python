import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
import string

# Завантажуємо необхідні пакети для токенізації та фільтрації стоп-слів
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')  # Завантаження пунктуального токенізатора

# Завантажуємо текст
with open('blake-poems.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Токенізація тексту (розбиваємо текст на слова)
words = word_tokenize(text)

# Визначення кількості слів у тексті
word_count = len(words)
print(f"Кількість слів у тексті: {word_count}")

# Підрахунок частоти всіх слів
word_frequencies = Counter(words)

# Визначення 10 найбільш вживаних слів (включно зі знаками пунктуації)
most_common_words = word_frequencies.most_common(10)
print(f"10 найбільш вживаних слів: {most_common_words}")

# Побудова стовпчастої діаграми для 10 найбільш вживаних слів
words_list, counts = zip(*most_common_words)
plt.figure(figsize=(10, 6))
plt.bar(words_list, counts, color='skyblue')
plt.title('Топ-10 найбільш вживаних слів')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))

# Фільтрація тексту від пунктуації та стоп-слів
filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

# Підрахунок частоти слів після фільтрації
filtered_word_frequencies = Counter(filtered_words)

# Визначення 10 найбільш вживаних слів після видалення стоп-слів
most_common_filtered_words = filtered_word_frequencies.most_common(10)
print(f"10 найбільш вживаних слів після видалення стоп-слів: {most_common_filtered_words}")

# Побудова стовпчастої діаграми для 10 найбільш вживаних слів після видалення стоп-слів
filtered_words_list, filtered_counts = zip(*most_common_filtered_words)
plt.figure(figsize=(10, 6))
plt.bar(filtered_words_list, filtered_counts, color='orange')
plt.title('Топ-10 найбільш вживаних слів (без стоп-слів та пунктуації)')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.show()
