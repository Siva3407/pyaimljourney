#in today topic we are gonna see about the int() float() bool() and str() and input() and also we are gonna find the age by this simple datatypes
ages= 16
name ="siva"
is_student= True
print(ages)
print(name)
print(is_student)
#age calculator by simple input functions
birthyr=int(input("enter the year of the birth:"))
currentyr=int(input("enter the current year:"))
currentmon=int(input("enter the current month(1-12):"))
birthmon=int(input("enter the birth month(1-12):"))
age=currentyr-birthyr
if currentmon<birthmon:
    age=age-1
print(age)
