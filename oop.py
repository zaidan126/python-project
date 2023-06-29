class Person:
    def __init__(self,name:str,age:int,gender:str):
        self.name=name
        self.age=age
        self.gender=gender
    def eat(self,food:str,amount:int):
        print(self.name,"eat",amount,"plate of",food)

class Student(Person):
    def learn(self,time:int,subject:str):
        print(self.name,"learn",subject,"at",time,"o'clock")