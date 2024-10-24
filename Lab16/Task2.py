import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів для NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


# Функція для обробки тексту
def process_text(input_file, output_file):
    try:
        # Читання тексту з вхідного файлу
        with open(input_file, 'r') as file:
            text = file.read()
            print("Вхідний файл успішно прочитаний.")
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено!")
        return

    # Токенізація по словам
    words = word_tokenize(text)

    # Лемматизація та стеммінг
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()

    # Видалення пунктуації та стоп-слів
    stop_words = set(stopwords.words('english'))
    words_processed = []

    for word in words:
        if word not in stop_words and word not in string.punctuation:
            # Лемматизація
            lemma_word = lemmatizer.lemmatize(word.lower())
            # Стеммінг
            stem_word = stemmer.stem(lemma_word)
            words_processed.append(stem_word)

    # Друк обробленого тексту в консоль
    print("Оброблений текст:", ' '.join(words_processed))

    # Запис обробленого тексту в інший файл
    try:
        with open(output_file, 'w') as file:
            file.write(' '.join(words_processed))
            print("Оброблений файл успішно записаний.")
    except IOError:
        print(f"Не вдалося записати файл {output_file}!")


# Виклик функції для обробки тексту
input_file = 'input_text.txt'  # Файл з довільним текстом до 100 слів
output_file = 'processed_text.txt'  # Файл для обробленого тексту

process_text(input_file, output_file)
