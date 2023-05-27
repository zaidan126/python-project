name= input("what is your name:")
age= int(input("what is your age:"))
#print(type(name),type(age))
if age<17:
    print("sorry ",name,", you are not allowed to get a driving licence")
elif age==17:
    email=input("pls input your parent email:")
    print("we aleady email to your parent(",email,"),after its confirmed then you can get your driving licence")
elif age>17 and age<100:
    print("here is your driving license")
    print("-"*50)
    print("I name:",name," "*50,"")
    print("I age:",age," "*50,"")
    print("-"*50)
else:
    print("your age is invalid")