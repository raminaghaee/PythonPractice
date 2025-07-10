############Sample Creatinine Clearance
age = input("Please enter your age: ")
weight = input("Please enter your weight: ")
serumCr = input("Please enter your serumCr: ")
gender = input("Please enter your gender(male/female): ").strip().lower()


age = int(age)
weight = float(weight)
serumCr = float(serumCr)
gender = gender.lower()

CreatinineClearance = ((140 - age) * weight) / ( 72 *serumCr)
if gender == 'male':
    print ("Your Creatinine Clearance is :" ,CreatinineClearance)
elif gender == 'female':
    CreatinineClearance = CreatinineClearance * 0.85
    print ("Your Creatinine Clearance is :" ,CreatinineClearance)
else:
    print("Please enter your gender correctly.")


if CreatinineClearance >= 85 :
    print("Normal GFR")
elif CreatinineClearance < 85 :
    print("Warning GFR")
else:
    print("Abnormal GFR")
#*****************************