from characters.character import Character
from random import randint
import utils.utils as ut

class Player(Character):

    def hit(self, nameOfHit: str):
        baseCriticalChance = self.getCriticalChance()
        randomNum = randint(0,100)
        if nameOfHit == "leg":
            if randomNum > baseCriticalChance + 10:
                return self.getAttackDamage() - (self.getAttackDamage()/2)
            else:
                return self.getAttackDamage() * 2
        elif nameOfHit == "hand":
            if randomNum > baseCriticalChance:
                return self.getAttackDamage()
            else:
                return self.getAttackDamage() * 2

        elif nameOfHit == "weapon":
            if self.isWeaponInUse:
                return self.weapon.getDamageOfHit()
        else:
            return 0