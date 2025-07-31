x = 200

def scope():
    x = 300
    print(x) #return 300
scope()
print(x) #return 200

"""
global
با استفاده از کلمه کلیدی گلوبال اون متغییر در تمام اون برنامه دیده میشه و اگر حتی درون فانکشنی استفاده بشه
به به همان خانه از حافظه اشاره میکنه
"""
y = 200
def scope2():
    global y
    y = 300
    print(y) #return 300
scope2()
print(y) #return 300

