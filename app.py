import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as OpenpyxlImage

# 1. Завантаження даних
df = pd.read_excel("sample_superstore.xlsx", sheet_name="Orders")

# 2. Попередня обробка
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Quarter'] = df['Order Date'].dt.to_period('Q')
df['Customer ID'] = df['Customer ID'].astype(str)

# 3. Визначення когорти
first_purchase = df.groupby('Customer ID')['Order Date'].min().reset_index()
first_purchase.columns = ['Customer ID', 'First Purchase']
first_purchase['Cohort'] = first_purchase['First Purchase'].dt.to_period('Q')
df = df.merge(first_purchase[['Customer ID', 'Cohort']], on='Customer ID')

# 4. Розрахунок LTV (прибуток на клієнта)
cohort_grouped = df.groupby(['Cohort', 'Year']).agg(
    customers=('Customer ID', 'nunique'),
    total_sales=('Sales', 'sum')
).reset_index()
cohort_grouped['LTV'] = cohort_grouped['total_sales'] / cohort_grouped['customers']

# 5. Підготовка до теплової карти
ltv_pivot = cohort_grouped.pivot(index='Cohort', columns='Year', values='LTV')

# 6. Побудова теплової карти
plt.figure(figsize=(10, 6))
sns.heatmap(ltv_pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title('Кумулятивна LTV (грн/клієнт) за кварталами долучення та роками')
plt.ylabel('Когорта (Квартал долучення)')
plt.xlabel('Рік')
plt.tight_layout()
plt.savefig("ltv_heatmap.png")
plt.close()

# 7. Експорт в Excel
excel_file = "cohort_ltv_output.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    cohort_grouped.to_excel(writer, sheet_name="Cohort_LTV", index=False)
    ltv_pivot.to_excel(writer, sheet_name="LTV_Heatmap")

# 8. Додавання картинки до Excel
wb = load_workbook(excel_file)
ws = wb["LTV_Heatmap"]
img = OpenpyxlImage("ltv_heatmap.png")
img.anchor = "G2"  # де розмістити зображення в Excel
ws.add_image(img)
wb.save(excel_file)

print(f"✅ Файл '{excel_file}' створено з тепловою картою")

