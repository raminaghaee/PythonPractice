"""این کتابخانه باعث میشود دیتا ها رو مثل یک فایل اکسل و حداثر به صورد 2 بعدی درون پایتون استفاده کنیم"""
from unittest.mock import inplace

#pip install pandas

import numpy as np
import pandas as pd

arr = np.array([0, 1, 2, 3])
labels = ['a', 'b', 'c', 'd']
series1 = pd.Series(data = arr, index = labels)
print(series1)
print(series1.shape)
"""
a    0
b    1
c    2
d    3
dtype: int64
(4,)
"""
"""در این نمونه یک دیتا یک بعدی با 4 تا دیتا داریم"""


dict1 = {"Name" : "Ramin", "Age" :30}
series2 = pd.Series(data = dict1)
print(series2)
"""
Name    Ramin
Age        30
dtype: object
"""

#DataFrame  return Date 2D
arr2 = np.random.randint(0, 20, size =(5,5))
print(arr2)

df1 = pd.DataFrame (arr2,['A','B','C','D','E'], ['a','b','c','d', 'e'])
print(df1)
"""
    a   b  c  d   e
A  10  10  0  8  10
B   9   4  1  1  18
C  14  14  2  2   3
D  15   4  1  0   5
E   4  15  4  0   4

"""

#Combine
dict2 = {"Name" : "Ramin", "Age" :30}
dict3 = {"Name" : "Zahra", "Age" :50}
df2 = pd.DataFrame({"Ramin": dict2, "Zahra" : dict3})
print(df2)
"""
      Ramin  Zahra
Name  Ramin  Zahra
Age      30     50
"""
print(df2['Zahra']['Age'])
#return 50




### Loc and Iloc
#loc
"""ردیفی که اون ستون توش قرار داره رو برمیگردونه"""
print(df2.loc['Age'])
"""
Ramin    30
Zahra    50
Name: Age, dtype: object
"""

#iloc
"""اندکس عددی میگیرد"""
"""اون ستون رو برمیگردونه"""
print(df2.iloc[1])
"""
Ramin    30
Zahra    50
Name: Age, dtype: object
"""

####T Method
"""با صدا زدن متد T جای ستون ها و ردیف ها با هم عوض میشن"""
print(df2.T)
"""
        Name Age
Ramin  Ramin  30
Zahra  Zahra  50

باید درون یک متغیر ریخته شود تا مقدارش باقی بمونه
"""

#گرفتن ستون های خاص
print(df1[['a','b','c']])
"""
    a   b   c
A   6   9   9
B   2   8   3
C   3   9  11
D  19  12   1
E   5  19   2
"""

#دریافت ردیف خاص
print(df1.loc[['A','B']])
"""
    a   b  c   d  e
A  19  10  1   7  6
B   3  17  3  13  2
"""


##addlist
series3 = df1['a']
df1['f'] = series3
print(df1)
"""
    a   b   c   d   e   f
A   3  12  18   7   1   3
B   6  11   9  12  18   6
C  16   4   6  10  15  16
D   9   8   6  10  16   9
E   4   2   8  17  10   4
"""

df1 =df1 *2
print(df1)
#or
df1['f'] = df1['f'] /2
print(df1)

#sum
df1['g'] = df1['b'] + df1['a']
print(df1)


#####Mask
"""فقط اون دیتایی که میخواهیم رو نمایش بده"""
print(df1[df1>30])
"""
    a     b     c     d     e   f     g
A NaN   NaN   NaN  32.0   NaN NaN   NaN
B NaN  36.0   NaN   NaN   NaN NaN  52.0
C NaN  38.0   NaN   NaN   NaN NaN  52.0
D NaN   NaN  36.0   NaN  32.0 NaN   NaN
E NaN   NaN   NaN   NaN  34.0 NaN   NaN
"""
"""NaN همون null هست"""



####Remove Date
print(df1.shape)
#return (5, 7)
"""به هر کدام از این عدد هایی که متد shape برمیگردونه یک axis گفته میشود که از 0 شروع میشود و به اشاره به ردیف داره"""
"""
axis = 0 => row
axis = 1 => column
...

"""
print(df1.drop("f",axis= 1))
#ستون f را حذف کرد
"""به axis خیلی باید توجه شود اگر اشتباه وارد شود خطرناک است و اگر اون ستون یا ردیف هدف وجود نداشته باشد خطا میدهد"""


###inplcae
"""یکی از ورودی های متدها،  پارامتر inplcae هستش که اگر مقدار true داشته باشد هر عملیاتی در اون دیتافریم بدون اینکه درون متغییر دیگر ریخته شود ذخیره میماند"""
df1.drop("f",axis = 1,inplace = True)
print(df1)



####Mean / Max / Min
"""میتوان میانگین و مکزیمم و مینیمم یک ستون یا ردیف رو هم حساب کرد"""
print(df1['g'].mean())

####NaN or Null
"""در هوش مصنوعی مقدار خالی و یه null و یا NaN خطرناک است و خیلی باید حواسمان باشد"""
print(df1[df1>30].isnull())
#or isna()
print(df1[df1>30].isna())

"""هر ستون چند تا null داره"""
print(df1[df1>30].isnull().sum())


#######fillna
"""در جاهایی که Nan هستش میاد مقدار ورودی را قرار میدهد"""
print(df1[df1>30].fillna(0, inplace = True))
