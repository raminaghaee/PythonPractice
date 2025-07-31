def name():
    print("Name")


def name1(n):
    print(n)

name1("Ramin")
#return => Ramin

def double(n):
    print(n*2)

double(3)
#return => 6

test1 = double(3)
print(test1)
""" Return  =>
6
none   => خودش دستور پرینت داره پس وقتی روی متغیرش پرینت بزنی چیزی برنمیگردونه
برای حل این مشکل باید از ریترن استفاده بشه
rutern
"""

def double1(n):
    return n*2

bist = double1(10)
print(bist)
#retrun  : 20


"""Sample GFR"""
def GFR(w,a,cr,g):
    if g == "male":
        return (( 140 - a ) * w ) / 72 * cr
    elif g == "female":
        return (((140 - a ) * w ) / 72 * cr ) * 0.85
    else:
        print("Please enter a valid gender")

raminGFR = GFR(90, 30,1.3,"female")
print(raminGFR)


"""Use Multipale Argument"""
"""
Sample 1
Type n = Touple  by *n
"""
def Printer(*n):
    print(*n) #return => 1 2 3 4
    print(n) # return touple => (1, 2, 3, 4)

Printer(1,2,3,4)

"""
Sample 2
type a => Key Word Argument by **a 
"""
def PrinterKW(**a):
    print(a) #return => {'name': 'Ramin', 'age': 35, 'gender': 'male'}
    print(*a) #return => name age gender
    print(*a.values())  # return => Ramin 35 male
    print(*a.items())  # return => ('name', 'Ramin') ('age', 35) ('gender', 'male')

PrinterKW(name="Ramin", age=35, gender="male")



"""Sample Max"""
def PrinterMax(*a):
    flags_Max = a[0]
    for x in a[1:]:
        if x > flags_Max:
            flags_Max = x
    return (flags_Max)

print(PrinterMax(1,2,3,4)) #retrun => 4

"""Warnnig"""
my_list = [1,2,3,4,5,6,7,8,9]
print(PrinterMax(my_list))
"""
return : [1, 2, 3, 4, 5, 6, 7, 8, 9]
 دقت شود در این حالت که یک لیست داریم بهش میدیم خود اون لیست رو به عنوان 
یک ارگومان در نظر میگیره
و اگه بخواهیم به محتویات 
درون خود آرگومان هم دست رسی داشته باشیم با یک بار هم روی خود اون لیست حلقه بزنیم 
"""
def PrinterMax2(*a):
    if type(a[0]) == list:
        flags_Max = PrinterMax2(*a[0])
    else:
        flags_Max = a[0]
    for x in a[1:]:
        if type(x) == list:
            flags_Max = PrinterMax2(*x)
        elif x > flags_Max:
            flags_Max = x
    return (flags_Max)

print(PrinterMax2([55,13,107,-256],3,[1007,2000]))



"""Sample 3"""
def PrinterMax3(*a):
    flags_Max = -float('inf')  # مقدار اولیه را بینهایت منفی قرار می‌دهیم
    for x in a:
        if type(x) == list:
            current_max = PrinterMax3(*x)
            if current_max > flags_Max:
                flags_Max = current_max
        elif x > flags_Max:
            flags_Max = x
    return flags_Max

print(PrinterMax3([55,13,107,-256,3000],3,[1007,2000]))  # خروجی صحیح: 3000



"""Sample Fibonacci()"""
def Fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(Fibonacci(20))
#return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]