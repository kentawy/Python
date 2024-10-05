import pandas as pd
import matplotlib.pyplot as plt
import os


def load_data():
    # Завантаження даних
    input_file = 'gdp_per_capita.csv'  # Ім'я вхідного файлу
    try:
        # Читання CSV файлу
        df = pd.read_csv(input_file)

        # Перевірка, чи містить файл необхідні дані
        if df.empty:
            print("Помилка: Дані відсутні у файлі.")
            return None

        # Видалення рядків, де всі значення є NaN
        df = df.dropna(how='all')
        return df
    except FileNotFoundError:
        print(f"Помилка: Файл '{input_file}' не знайдено.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Помилка: Файл '{input_file}' порожній.")
        return None
    except pd.errors.ParserError:
        print(f"Помилка: Файл '{input_file}' має неправильний формат.")
        return None


def plot_gdp_trends(df):
    # Фільтрація даних для США та України
    gdp_usa = df[df['Country Name'] == 'United States'].iloc[0, 4:].astype(float)
    gdp_ukr = df[df['Country Name'] == 'Ukraine'].iloc[0, 4:].astype(float)

    years = df.columns[4:]

    # Побудова графіку
    plt.figure(figsize=(12, 6))
    plt.plot(years, gdp_usa, label='США', marker='o')
    plt.plot(years, gdp_ukr, label='Україна', marker='o')

    plt.title('Динаміка GDP на душу населення (2000-2020)')
    plt.xlabel('Рік')
    plt.ylabel('GDP на душу населення (current US$)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


def plot_bar_chart(df, country_name):
    # Фільтрація даних за країною
    country_data = df[df['Country Name'] == country_name]

    if country_data.empty:
        print(f"Дані для країни '{country_name}' відсутні.")
        return

    gdp_values = country_data.iloc[0, 4:].astype(float)

    # Побудова стовпчастої діаграми
    plt.figure(figsize=(10, 5))
    plt.bar(gdp_values.index, gdp_values, color='skyblue')

    plt.title(f'GDP на душу населення для {country_name} (2000-2020)')
    plt.xlabel('Рік')
    plt.ylabel('GDP на душу населення (current US$)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


def main():
    df = load_data()
    if df is not None:
        plot_gdp_trends(df)

        while True:
            # Введення назви країни для стовпчастої діаграми
            country_name = input(
                "Введіть назву країни для побудови стовпчастої діаграми (наприклад, 'Ukraine' або 'United States'), або введіть 'exit' для виходу: ")
            if country_name.lower() == 'exit':
                print("Вихід з програми.")
                break
            plot_bar_chart(df, country_name)


if __name__ == "__main__":
    main()
