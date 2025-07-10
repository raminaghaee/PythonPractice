print (type("2"))
print (type(int("2")))
print (type(float("2.2")))
#Run time error : don't cast Large number to small number And Don't Cast Float number to in
#print (type(int("2.2")))
print (type(str(3.1)))



h = input("Please enter a height in cm: ")
w = input("Please enter a weight in kg: ")

print ("before cast",type(h))
print ("before cast",type(w))

h = float(h)
w = float(w)

print ("After cast",type(h))
print ("After cast",type(w))

bmi = (w / ( h /100 ) ) ** 2
print ("Your BMI is" , bmi)