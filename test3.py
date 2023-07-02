from oop2 import*
player=Mage("zaidan",120,310)
monster=Slime("slime",50,71)
player.attack(monster)
monster.showstatus()
player.plasma_beam(monster)
player.showstatus()
player.plasma_heal(player)
player.showstatus()
for i in range(7):
    monster.Slime_ball(player)
monster.showstatus()
player.showstatus()
for i in range(7):
    player.plasma_beam(monster)
    monster.showstatus()