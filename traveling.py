country= input("pick a country where you want to travel: ")
if country== "America":
    city= input("pick a city: ")
    if city== "New york":
        print("welcome to new york")
        hotel= input("pick a hotel: ")
        if hotel== "insignia":
            print("welcome to city hotel")
        elif hotel== "luxe studio":
            print("welcome to our villa")
    elif city== "los angeles":
        print("welcome to los angeles")
        hotel= input("pick a hotel: ")
        if hotel== "double tree":
            print("welcome to our city hotel")
elif country == "Russia":
    city= input("pick a city:")
    if city== "Moscow":
        print("welcome to Moscow")
        hotel= input("pick a hotel:")
        if hotel== "four season hotel":
            print("welcome to city hotel")
        elif hotel== "Lesnoy home":
            print("welcome to our villa")
    elif city== "Stalingrad":
        print("welcome to stalingrad")
        hotel= input("pick a hotel: ")
        if hotel== "volgograd":
            print("welcome to volgograd")
elif country == "Uk":
    city= input("pick a city: ")
    if city== "London":
        print("welcome to London")
        hotel= input("pick a hotel: ")
        if hotel== "the tower hotel":
            print("welcome to our city hotel")
        elif hotel== "villa collective":
            print("welcome to our villa")
    elif city== "Birmingham":
        print("welcome to Birmingham")
        hotel= input("pick a hotel: ")
        if hotel== "hyatt regency":
             print("welcome to our city hotel")


       
else: print("im sorry the country not detected")