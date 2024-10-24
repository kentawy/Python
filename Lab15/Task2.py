import pandas as pd
import matplotlib.pyplot as plt

# Завантажуємо дані з файлу CSV (замініть шлях на правильний)
file_path = 'comptagevelo2010.csv'

# Завантаження даних у DataFrame
df = pd.read_csv(file_path)

# Попереднє форматування стовпця 'Date' для зручності аналізу
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Фільтруємо дані тільки для перших трьох днів січня
filtered_df = df[df['Date'].dt.strftime('%Y-%m-%d').isin(['2010-10-08', '2010-09-10', '2010-12-29'])]

# Маппинг колонок на их новые названия
columns_mapping = {
    'Berri1': 'Berri 1',
    'Brébeuf': 'Brbeuf (donnes non disponibles)',
    'CSC (Côte Sainte-Catherine)': 'Cte-Sainte-Catherine',
    'Maisonneuve_1': 'Maisonneuve 1',
    'Maisonneuve_2': 'Maisonneuve 2',
    'Parc': 'du Parc',
    'PierDup': 'Pierre-Dupuy',
    'Rachel / Papineau': 'Rachel1'
}

# Переименовываем колонки и выбираем нужные
filtered_df = filtered_df[['Date'] + list(columns_mapping.keys())].rename(columns=columns_mapping)

# Показ таблицы данных, похожей на картинку
print(filtered_df)

# Створимо новий стовпець 'Month' для агрегації по місяцях
df['Month'] = df['Date'].dt.month

# Агрегуємо дані: кількість велосипедистів по місяцях для доріжки Berri 1
monthly_usage = df.groupby('Month')['Berri1'].sum()

# Визначаємо місяць з найбільшою кількістю велосипедистів
best_month = monthly_usage.idxmax()
max_cyclists = monthly_usage.max()

print(f"Найбільш популярний місяць: {best_month}, з кількістю велосипедистів: {max_cyclists}")

# Побудова графіку
plt.figure(figsize=(10, 6))
monthly_usage.plot(kind='bar', color='skyblue')
plt.title('Кількість велосипедистів на велодоріжці Berri1 за місяцями (2010)')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.xticks(rotation=0)
plt.grid(True)

# Показуємо графік
plt.tight_layout()
plt.show()
