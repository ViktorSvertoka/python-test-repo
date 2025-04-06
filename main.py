import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Завантаження Excel-файлу з даними
df = pd.read_excel("./sample_superstore.xlsx", sheet_name="Orders")

# Перетворення дати замовлення та виділення місяця
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['OrderMonth'] = df['Order Date'].dt.month

# Підрахунок обсягу продажів по місяцях
monthly_totals = df.groupby('OrderMonth')['Sales'].sum()

# Побудова діаграми: розподіл продажів протягом року
plt.figure(figsize=(9, 4))
monthly_totals.plot(kind='bar', color='#4C72B0')
plt.title('Продажі по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Обсяг продажів')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("monthly_sales_distribution.png")
plt.show()

# Виявлення екстремальних значень у продажах
q1 = df['Sales'].quantile(0.25)
q3 = df['Sales'].quantile(0.75)
iqr = q3 - q1
bounds = 1.5 * iqr
outliers = df[(df['Sales'] < (q1 - bounds)) | (df['Sales'] > (q3 + bounds))]

print(f"Кількість транзакцій з відхиленнями: {len(outliers)}")

# Зведення ключових метрик по споживацьких сегментах
segment_summary = df.groupby('Segment').agg(
    avg_sales=('Sales', 'mean'),
    med_sales=('Sales', 'median'),
    sales_std=('Sales', 'std'),
    total_profit=('Profit', 'sum')
)

print("\nПоказники по клієнтських сегментах:")
print(segment_summary)

# Кругова діаграма розподілу продажів між категоріями
plt.figure(figsize=(6, 6))
df.groupby('Category')['Sales'].sum().plot.pie(
    autopct='%1.0f%%',
    startangle=90,
    explode=[0.08, 0, 0],
    colors=['#66c2a5', '#fc8d62', '#8da0cb']
)
plt.ylabel('')
plt.title('Частка продажів за типами товарів')
plt.tight_layout()
plt.savefig("category_pie_chart.png")
plt.show()

# Експорт результатів в Excel
with pd.ExcelWriter("analytics_output.xlsx") as writer:
    df.describe().to_excel(writer, sheet_name="Summary")
    outliers.to_excel(writer, sheet_name="Outlier_Sales", index=False)
    segment_summary.to_excel(writer, sheet_name="Segment_Stats")

print("Файл analytics_output.xlsx успішно створено.")
