#today we are gonna do the bmi calcutor using the simple arithmetic assignment comparison and logical operators
weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in m:"))
bmi=weight/(height*height)
print("your bmi is:",round(bmi,2))
if bmi<18.5:
    print("you are underweight")
elif bmi>=18.5 and bmi<24.9:
    print("you are normal weight")
elif bmi>=25 and bmi<29.9:
    print("you are over weight")
else:
    print("you are obese")