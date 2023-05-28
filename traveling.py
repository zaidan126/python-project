country= input("pick a country where you want to travel: ")
if country== "America":
    city= input("pick a city:")
    if city== "New york":
        print("welcome to new york")
        hotel= input("pick a hotel:")
        if hotel== "insignia":
            print("welcome to city hotel")
        elif hotel== "luxe studio":
            print("welcome to our villa")
    elif city== "los angeles":
        print("welcome to los angeles")
elif country == "Russia":
    pass
elif country == "Uk":
    pass
else: print("im sorry the country not detected")