"""
ییلد  وقتی در یک تابع استفاده میشود وقتی به اولین ییلد میرسد دیتارو برمیگردونه و وقتی دوباره اون تابع صدا زده بشه میره سراغ ییلد بغدی

تابع های دارای yield رو نمیشه خالی صدا زد و خطا میده و باید از تابغ پیمایش گرد زیر استفاده شود
next(تابع)
نکته مهمی که داره اینکه باید نتیجه اولین بار اجرا شدن این تابع next رو بریزیم داخل یک متغییر
و حالا به ازای هر بار صدا زدن آن متغییر همراه با next میره سراغ yield بعدی

در صورت عدم صدا زدن تابع next ، خطا زیر ایجاد میشود
<generator object char at 0x000002263FE65FE0>

"""
def char():
    yield "R"
    yield "a"
    yield "m"
    yield "i"
    yield "n"

#اشتباه
print(next(char())) # return R
print(next(char())) # return R
print(next(char())) # return R
print(next(char())) # return R
print(next(char())) # return R


#صحیح
chars = char()
print(next(chars)) # return R
print(next(chars)) # return a
print(next(chars)) # return m
print(next(chars)) # return i
print(next(chars)) # return n
"""print(next(chars))  Error"""

"""
این نوع پیمایش هم اگر به آخرش برسیم و دیتا دیگه ای نباشه و بخواد صداش بزنه خطا میده

برای همین بهترین راهکار استفاده از for برای پیمایش در رابطه با این نوع خطاست 

"""

chars1 = char()
for char in chars1:
   print(char)


"""Sample fibonacci us by yield"""

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fibo = fib()
print(next(fibo)) #0
print(next(fibo)) #1
print(next(fibo)) #1
print(next(fibo)) #2

fibo1 = fib()
for _ in range(10) :
    print(next(fibo1))
"""
0
1
1
2
3
5
8
13
21
34
"""