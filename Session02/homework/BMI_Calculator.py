mass = int(input("Ban nang bao nhieu kg: "))
height = int(input("Ban cao bao nhieu cm: "))
bmi = 10000*mass / (height*height)
print ("Your BMI: " ,bmi)
if bmi < 16:
    print ("Severely underweight")
elif bmi < 18.5:
    print ("Underweight")
elif bmi < 25:
    print ("Normal")
elif bmi <= 30:
    print ("Overweight")
else: print ("Obese")             
