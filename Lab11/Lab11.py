import pandas as pd
import os


def main():
    input_file = 'GDP_per_capita_USA_1991_2019.csv'  # Ім'я вхідного файлу
    output_file = 'GDP_per_capita_USA_Min_Max.csv'  # Ім'я вихідного файлу

    # Вивід поточної робочої директорії для діагностики
    print("Поточна робоча директорія:", os.getcwd())

    try:
        # Читання CSV файлу, пропускаючи останні 4 рядки з метаданими
        df = pd.read_csv(input_file, skipfooter=4, engine='python')

        # Видалення рядків, де всі значення є NaN
        df = df.dropna(how='all')
    except FileNotFoundError:
        print(f"Помилка: Файл '{input_file}' не знайдено.")
        return
    except pd.errors.EmptyDataError:
        print(f"Помилка: Файл '{input_file}' порожній.")
        return
    except pd.errors.ParserError:
        print(f"Помилка: Файл '{input_file}' має неправильний формат.")
        return
    except Exception as e:
        print(f"Сталася невідома помилка: {e}")
        return

    # Вивід перших кількох рядків для перевірки
    print("Вміст CSV файлу:")
    print(df)

    # Перевірка, чи містить файл необхідні дані
    if df.empty:
        print("Помилка: Дані відсутні у файлі.")
        return

    # Витягування рядків з даними про GDP
    try:
        # Виділяємо стовпці з роками
        year_columns = [col for col in df.columns if col.startswith('199') or col.startswith('20')]

        # Перетворення даних у довгий формат
        data_df = df.melt(id_vars=['Country Name', 'Country Code'],
                          value_vars=year_columns,
                          var_name='Year',
                          value_name='GDP per capita (current US$)')

        # Видалення рядків з NaN значеннями у GDP
        data_df = data_df.dropna(subset=['GDP per capita (current US$)'])

        # Перетворення Year з формату '1991 [YR1991]' у '1991'
        data_df['Year'] = data_df['Year'].str.split().str[0]
    except Exception as e:
        print(f"Помилка при перетворенні даних: {e}")
        return

    # Вивід усіх років і значень ВВП
    print("\nВсі дані GDP per capita (current US$) для США за 1991-2019 роки:")
    print(data_df)

    # Знаходження мінімального та максимального значень ВВП на душу населення
    min_value = data_df['GDP per capita (current US$)'].min()
    max_value = data_df['GDP per capita (current US$)'].max()

    # Знаходження років, коли були досягнуті мінімум та максимум
    min_years = data_df.loc[data_df['GDP per capita (current US$)'] == min_value, 'Year'].tolist()
    max_years = data_df.loc[data_df['GDP per capita (current US$)'] == max_value, 'Year'].tolist()

    # Підготовка даних для запису у новий CSV файл
    result = {
        'Показник': ['Найнижчий', 'Найвищий'],
        'Рік': [
            ', '.join(min_years) if min_years else 'N/A',
            ', '.join(max_years) if max_years else 'N/A'
        ],
        'GDP per capita (current US$)': [min_value, max_value]
    }

    result_df = pd.DataFrame(result)

    # Вивід результатів для перевірки
    print("\nРезультати пошуку:")
    print(result_df)

    try:
        # Запис результатів у новий CSV файл
        result_df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"\nРезультати успішно записані у файл '{output_file}'.")
    except Exception as e:
        print(f"Не вдалося записати файл '{output_file}': {e}")


if __name__ == "__main__":
    main()
