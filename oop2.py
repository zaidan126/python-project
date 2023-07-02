class Character:
    def __init__(self,name:str,HP:int,MP:int):
        self.name=name
        self.HP=HP
        self.MP=MP
    def attack(self,enemy):
        enemy.HP-=3
        print(self.name,"attack",enemy.name)
    def showstatus(self):
        if self.HP>0:
            print(self.name,"\'s HP:",self.HP)
            print(self.name,"\'s MP:",self.MP)
        else:
            print(self.name,"died")
class Mage(Character):
    def plasma_beam(self,enemy):
        if self.MP>=15:
            enemy.HP-=21
            self.MP-=15
            print(self.name,"use plasma beam to",enemy.name)
        else:
            print(self.name,"not enough MP")
    def plasma_heal(self,character):
        if self.MP>=37:
            character.HP+=50
            self.MP-=37
            print(self.name,"use plasma heal to",character.name)
        else:
            print(self.name,"not enough MP")
class Slime(Character):
    def attack(self, enemy):
        enemy.HP-=20
        print(self.name,"slime quake",enemy.name)
    def Slime_ball(self,enemy):
        if self.MP>=14:  
            enemy.HP-=23
            self.MP-=14
            print(self.name,"use slime ball to",enemy.name)
        else:
            print(self.name,"not enough MP")