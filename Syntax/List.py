list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = ["Ramin" , "Zahra" , "Mohamad" , " Reza"]
list3 = ["math", 12 , "history" , 20.0]
list4 = [[12,3,45],[23,44,2],[23,55,77]]

###Len
print("################################ Len")
print(len(list1))
print(len(list4))

##Index
print("################################ Index")
print(list4[1])
print(list1[-1])
print(list1[1:6])
#return [1, 2, 3, 4, 5]

print(list1[:6])
#return [0, 1, 2, 3, 4, 5]

print(list1[1:9:2])
#return [1, 3, 5, 7]

print(list1[0:-2])
#return [0, 1, 2, 3, 4, 5, 6, 7]

print(list1[-2:])
#return [8, 9]

print(list1[10:0:-1])
#return [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(list1[-5:])
#return [5, 6, 7, 8, 9]

print(list1[-5:-10:-1])
#return [5, 4, 3, 2, 1]

print(list1[::3])
#return [0, 3, 6, 9]
'''دو تا درمیون نشون میده'''



## Insert and Append and Remove
print("####################### Insert and Append and Remove and pop and clear and copy and Reverse and Sort")

'''insert to end index'''
list2.append("Hossein")
print(list2)

'''insert item to index'''
list2.insert(1,"Hassan")
print(list2)

''' اولین آیتمی که پیدا میکنه رو حذف میکنه'''
'''حذف بر اساس دیتا'''
list5 = ["Ramin" , "Zahra" , "Mohamad" , "Ramin", " Reza"]
list5.remove("Ramin")
print(list5)

list6 = ["Ramin" , "Zahra" , "Mohamad" , "Ramin", " Reza"]
'''Remove item by index'''
list6.pop(-1) #or .pop() remove end index
print(list6)
# return ['Ramin', 'Zahra', 'Mohamad', 'Ramin']


'''Remove all item from list'''
list6.clear()
print(list6)

'''Copy'''
list7 = ["Ramin" , "Zahra" , "Mohamad" , "Ramin", " Reza"]
'''در این تو ریختن لیست در لیست دیگر هر دو به یک خانه از حافظه اشاره میکنن و لذا تغییر در یک لیست
در لیست دیگر نیست تاثیر دارد'''
list8 = list7
print(list8)
list7.clear()
print(list8)
##return :  []

list9 = ["Ramin" , "Zahra" , "Mohamad" , "Ramin", " Reza"]
list10 = list9.copy()
list9.clear()
print(list10)


##Reverse
list11 = [23,5234,1,234,3,556,10]
list11.reverse()
print(list11)
##### or print(list11[::-1])


########################Sort
list11.sort()
print(list11)
list11.sort(reverse=True)
print(list11)


'''عدد و رشته همزمان نمیتونن مرتب سازی روشون اجرا بشه'''
'''برای مرتب سازی باید عدد ها رو هم به صورت رشته نوشت تا بتونه مرتب سازی بر اسا کد آسکی ان ها انجام بشه'''

list12 =["Ramin" , "Zahra","2","55","6546" , "Mohamad" ,"42", "Ramin", "Reza"]
list12.sort()
print(list12)

'''دقت شود که رشته ها نباید اولشون فاصله داشته باشن وگرنه درست مرتب نمیشن و لر اساس خالی بودن اول رشته مرتب میشن'''
list13 = ["Ramin","5","3", " Reza"]
list13.sort()
print(list13)
#return : [' Reza', '3', '5', 'Ramin']


'''دقت شود که این مرتب سازی بر اساس حرف اول مرتب سازی صورت میگیرد و وقتی حرف اول یکسان باشد میره سراف حرف دوم'''

list14 = ["Ramin" , "2" , "1000" , "Reza"]
list14.sort()
print(list14)
#return : ['1000', '2', 'Ramin', 'Reza']

#or
list15 = [[12,3,45],[28,55,77],[23,12,11]]
list15.sort()
print(list15)
#return : [[12, 3, 45], [23, 12, 11], [28, 55, 77]]


##################### Sum
list16 = [1,2,3,4,5]
list17 = [2,3,4,5,6]
print(list16 + list17)
#return : [1, 2, 3, 4, 5, 2, 3, 4, 5, 6]

## or
#####extend
list16.extend(list17)
print(list16)
#return : [1, 2, 3, 4, 5, 2, 3, 4, 5, 6]

## or
list18 = [1,2,3,4,5]
list19 = [2,3,4,5,6]
for item in list19:
    list18.append(item)
print(list18)
#return : [1, 2, 3, 4, 5, 2, 3, 4, 5, 6]

###error
# list16 = [[12,3,45],3,[28,55,77],[23,12,11]]
# for i in list16:
#     for j in i:
#         print(j)
'''در این شرایط چون عدد 3 ایتر ایبیل نیستش یعنی قابل پیمایش نیست برای بوپ که نوشته شده
در نتیججه خطا طمان اجرا رخ میدهد
این خطا برای لوپ دوم هستش
 لوپ اول وقتی به ایندکس 1 میرسه عدد 3 رو نمیتونه در لوپ دوم به عنوان لیست قرار بده و پیمایشش کنه 
'''
'''راه حل'''
list16 = [[12,3,45],3,[28,55,77],[23,12,11]]
for i in list16:
    if type(i) == list or type(i) == str:
        for j in i:
            print(j)

