import pandas as pd
import numpy as np

"""dataframe"""
data = pd.read_csv('F:/Work/Python/AI 1404/Bioneers/Python/PythonPractice/Pandas/annual-enterprise-survey-2024-financial-year-provisional.csv')

print(data.head())
"""5 تا ردیف اول رو نشون میده"""

print(data.head(10))
"""10 تا ردیف اول رو نشون میده"""

print(data.tail())
"""5 تا ردیف آخر رو نشون میده"""


print(data.describe())
"""یک سری اطلاعات بهمون میده مثل میانگین و تعداد"""


#add Column
data['weight'] = np.random.randint(60,120, size=len(data))
data['height'] = np.random.randint(160,200, size=len(data))
print(data.head())


data['bmi'] = data['weight'] / ((data['height']  * 100) * 2)
print(data.head())

print(data[data['weight'] > 100])

n = 0
for col in data[data['weight'] > 100]['weight']:
    if col > 110:
        n += 1
print(n)

"""حذف دیتاتکراری"""
data.drop_duplicates(subset='weight', inplace=True)

"""ذخیره دیتا درون دایرکتوری"""
##### data.to_excel('path/FileName.xlsx')