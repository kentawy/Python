import os

# Функція для створення файлу TF8_1
def create_file_tf8_1(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        # Додаємо рядки різної довжини
        f.write("Привіт, це тестовий файл.\n")
        f.write("Тут є різні рядки.\n")
        f.write("12345\n")
        f.write("Python - чудова мова програмування.\n")
        f.write("Текст без цифр.\n")
        f.write("1234567890\n")
        f.write("Кінець файлу.\n")

# Функція для обробки файлу TF8_1 і запису в TF8_2
def process_file_tf8_1(input_filename, output_filename):
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

# Функція для виводу вмісту файлу TF8_2
def print_file_tf8_2(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.readlines()
        return [line.strip() for line in content]

# Основна частина програми
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
    for line in output_content:
        print(line)
