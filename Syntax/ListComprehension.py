########### List Comperation
'''لیست اعداد 0 تا 9 به توان 2'''
list1 = [i**2 for i in range(10)]
print(list1)


'''لیست اعداد 0 تا 9 در صورتی بر 2 بخش پذیر باشد'''
list2 = [i for i in range(10) if i%2 ==0]
print(list2)


