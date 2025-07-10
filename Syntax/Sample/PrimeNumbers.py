##########Prime numbers
"""
یعنی بر خودشون و یک بخش پذیر باشند
یعنی باقی مانده داشته باشد
و یا به عبارتی بر اعداد کوچک تر از خودش بخش پذیر نباشد به جز یک
"""


number = int(input("Please enter your number: "))
prime = True
for i in range(2,number):
    print(i)
    if number % i == 0 :
        prime = False
        break
if prime :
    print("Your number is prime")
else:
    print("Your number is not prime")
