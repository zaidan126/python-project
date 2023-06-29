import oop

zaidan=oop.Person("zaidan",10,"m")
carrent=oop.Person("carrent",900,"none")
zaidan.eat("SPICY NOODLE",90909090)
zaidan.eat("PIZZA",4)
carrent.eat("steak",5)
def getlicense(person):
    if(person.age<17):
        print(person.name,"cannot get the licensed because too young")
    else:
        print("here is your licensed mr/ms",person.name)
getlicense(zaidan)
zaidan2=oop.Student("zaidan",90,"m")
zaidan.eat("noodle",3)
zaidan2.learn(12,"english")
carrent.eat()