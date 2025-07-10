################  While
count = 5
while count > 0:
    count -= 1
    print(count)

# use break or continue
while count < 5:
    count += 1
    if count % 2 == 0:
        break #or continue
    print(count)


#Use Else Along with While
count2 = 5
while count2 > 0:
    count2 -= 1
    print(count2)
#وقتی اجرا میشود که شرط حلقه برقرار نباشد
else :
    print("end loops")


#در صورتی که شرط دارای بریک باشد اگر اجرا شود دستور الس اجرا نمیشود
#Use Else Along with While
count3 = 5
while count3 > 0:
    count3 -= 1
    print(count3)
    if count3 % 2 == 0:
        break
else :
    print("end loops")

#************************************

#################  for
##syntax1
my_list = ["Ramin" , "Zahra" , "Mohammad"]
for name in my_list:
    if name == "Zahra" :
        continue
    print(name)

###use range
for i in range(5):
    print(i)