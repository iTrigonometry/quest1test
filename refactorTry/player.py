from refactorTry.character import Character
from random import randint
import utills.utils as ut

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
                if randomNum > self.weapon.getCriticalChance():
                    return self.weapon.getAttackDamage()
                else:
                    return self.weapon.getAttackDamage() * 2
            else:
                ut.printMsg("Соси жопу ты даже не поинтересовался есть у тебя оружие или нет")
        else:
            return 0