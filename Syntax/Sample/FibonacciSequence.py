#### enter number  ==> print fibonacci sequence til that number
#0 1 1 2 3 5 8 13 21 ...
'''
0+1 =1
1+1 =2
1+2=3
2+3=5
3+5=8
5+8=13
8+13=21
'''
number = int(input("Enter a number: "))
a = 0
b = 1
flags = 0
print(a)
print(b)

for _ in range(number):
    flags = a
    a = b
    b = flags + b
    print(b)



########## OR
number = int(input("Enter a number: "))
a, b = 0, 1
print(a)
print(b)
for _ in range(number):
    a, b = b, a + b
    print(b)