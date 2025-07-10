#Scope
condition = True
if condition:
    print("Cond")
    print (condition)
    print( "Inside scope")
print("Outside scope")




###if elif else
score = 20
if score > 10:
    print("pass")
elif score < 10:
    print("failed")
else:
    print("he scored 10")



#and / or
condition1 = False
condition2 = True
if condition1 and condition2:
    print("and pass")
elif condition1 or condition2:
    print("or pass")

### not == !
condition3 = 0
if not condition3 == 1: ##  not   or  !=
    print("false")
