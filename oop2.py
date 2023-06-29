class Character:
    def __init__(self,name:str,HP:int,MP:int):
        self.name=name
        self.HP=HP
        self.MP=MP
    def attack(self,character):
        character.HP-=3
        print(self.name,"attack",character.name)
        print(character.name,"\'s HP:",character.HP)
class Mage(Character):
    def plasma_beam(self,)