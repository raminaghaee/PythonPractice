dict1 = {"name" : "ramin", "age" : 27}
print(dict1["name"]) #=>ramin
print(dict1["age"]) #=>27
print(dict1) #=>{'name': 'ramin', 'age': 27}

"""
مرتب سازی ندارند و مرتب سازی صورت نمیگیرد
در صورت دادن کلید تکراری خطا نمیدهد و کلید تکراری اولی را نمایش نمیدهد
"""
dict2 = {2 : "ramin", 1 : "Ali",3 :"Reza" ,"score" : 19.5}
print(dict2)

##type
print(type(dict2["score"])) ## => float

##add
dict2["weight"] = 89.5
print(dict2)

##{2: 'ramin', 1: 'Ali', 3: 'Reza', 'score': 19.5, 'weight': 89.5}


##update()
"""دیتا ورودی با استفاده از یک دیکشنری دارای کلید و مقدار از همان جنس باید باشد"""
dict2["weight"] = 79
print(dict2)

#or

dict2.update({"weight" : 69})
print(dict2)



"""همچنین اگر کلید وارد شدهوجود نداشته باشد میاد اون مقدار رو به دیکشنری اضافه میکنه"""
dict2.update( {"height" : "200"})
print(dict2)

##return => {2: 'ramin', 1: 'Ali', 3: 'Reza', 'score': 19.5, 'weight': 69, 'height': '200'}


###pop(key)
dict2.pop("height")


#####Loop
for i in dict2:
    print("key :", i,"value :" ,dict2[i])
# key : 2 value : ramin
# key : 1 value : Ali
# key : 3 value : Reza
# key : score value : 19.5
# key : weight value : 69


for k in dict2.values():
    print(k)
# ramin
# Ali
# Reza
# 19.5
# 69

for v in dict2.keys():
    print(v)
# 2
# 1
# 3
# score
# weight
for v in dict2.items():
    print(v)
# (2, 'ramin')
# (1, 'Ali')
# (3, 'Reza')
# ('score', 19.5)
# ('weight', 69)


"""در این حالت آیتم داره به صورت تاپل مقدار کی و وی رو پر میکنه که به ترتیب کی میشه کلید و وی میشه مقدار"""
for k,v in dict2.items():
    print(k,"=",v)
# 2 = ramin
# 1 = Ali
# 3 = Reza
# score = 19.5
# weight = 69

####copy()
"""به این متد مثل بقیه لیست ها در کپی کردن دقت شود"""





####Nested Dictionary
"""چندین دیکشنری درون همدیگه هستند."""

nestedDictionary = {
    "Child1" :{
        "name" : "Ramin",
        "age" : 27,
    },
    "Child2" :{
        "name" : "Reza",
        "age" : 20,
    },
    "Child3" :{
        "name" : "Ali",
        "age" : 35,
    }
}

print(nestedDictionary["Child1"])  #return => {'name': 'Ramin', 'age': 27}
print(nestedDictionary["Child1"]["name"]) #return => Ramin


for i in nestedDictionary:
    print(nestedDictionary[i]["name"])
# Ramin
# Reza
# Ali

for i,j in nestedDictionary.items():
    print(i,"=>",j)
# Child1 => {'name': 'Ramin', 'age': 27}
# Child2 => {'name': 'Reza', 'age': 20}
# Child3 => {'name': 'Ali', 'age': 35}




#####get()
print(dict2.get("score")) #=>19.5
print(nestedDictionary.get("Child1")) #=>{'name': 'Ramin', 'age': 27}




dict3 = {"name" : "ramin" , "age" : 27, "height" : 190}
value = input("enter your value")
x = False
for i in dict3.values():
    if str(i) == value:
        x = True
    if x:
        print("Hast")
    else:
        print("Nist")
