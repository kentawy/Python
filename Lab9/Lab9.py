import os

# Функція для створення файлу TF8_1 з обробкою помилок
def create_file_tf8_1(filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # Додаємо рядки різної довжини
            f.write("Привіт, це тестовий файл.\n")
            f.write("Тут є різні рядки.\n")
            f.write("12345\n")
            f.write("Python - чудова мова програмування.\n")
            f.write("Текст без цифр.\n")
            f.write("1234567890\n")
            f.write("Кінець файлу.\n")
        print(f"Файл '{filename}' успішно створено!")
    except IOError as e:
        print(f"Помилка при створенні файлу '{filename}': {e}")

# Функція для обробки файлу TF8_1 і запису в TF8_2 з обробкою помилок
def process_file_tf8_1(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
            lines = infile.readlines()
            current_line = ""
            line_number = 1

            for line in lines:
                # Пропускаємо цифри
                line = ''.join(filter(lambda x: not x.isdigit(), line))
                current_line += line.strip()  # Вирівнюємо рядок

                # Формуємо рядки по 10 символів
                while len(current_line) >= 10:
                    segment = current_line[:10]
                    current_line = current_line[10:]
                    # Записуємо рядок з порядковим номером
                    outfile.write(f"{line_number:5} {segment}\n")
                    line_number += 1

            # Якщо залишилися символи, записуємо їх, якщо рядок не порожній
            if current_line:
                outfile.write(f"{line_number:5} {current_line}\n")

        print(f"Файл '{input_filename}' успішно оброблено і записано в '{output_filename}'!")
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не знайдено!")
    except IOError as e:
        print(f"Помилка вводу/виводу при роботі з файлом '{input_filename}' або '{output_filename}': {e}")

# Функція для виводу вмісту файлу TF8_2 з обробкою помилок
def print_file_tf8_2(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.readlines()
            return [line.strip() for line in content]
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено!")
        return []
    except IOError as e:
        print(f"Помилка при читанні файлу '{filename}': {e}")
        return []

# Основна частина програми з обробкою помилок
if __name__ == "__main__":
    # Імена файлів
    tf8_1_filename = "TF8_1.txt"
    tf8_2_filename = "TF8_2.txt"

    # Створюємо файл TF8_1
    create_file_tf8_1(tf8_1_filename)

    # Обробляємо файл TF8_1 і записуємо в TF8_2
    process_file_tf8_1(tf8_1_filename, tf8_2_filename)

    # Виводимо вміст файлу TF8_2
    output_content = print_file_tf8_2(tf8_2_filename)
    if output_content:
        print("\nВміст файлу TF8_2:")
        for line in output_content:
            print(line)
