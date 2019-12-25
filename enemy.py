import random
#TODO добавить возможность экипировки оружия
#TODO характеристики в зависимости от врага или повышение характеристик по ходу игры
#
"""#LIST OF ENEMY
SVYATOY - Святой

"""
#класс врага 
class Enemy:


    def setEnemy(self):
        if self.name == "SVYATOY":
            self.hp = 100
            self.attackDamage = 1
            self.critChance = 10


    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attackDamage = 1
        self.critChance = 10

    

    def hit(self):
        """Метод атаки врага 
            Удар выбирается рандомно
            Если удар рукой, то обычный урон
            Если удар ногой, то урон х2
            Если удар оружием, то урон 0
        Returns:
            [int] -- [damage]
        """
        randomHit = random.randint(1,3)

        if randomHit == 1: return self.attackDamage
        else:
            if randomHit == 2: 
                randomNum = random.randint(0,100)
                if randomNum > self.critChance: return self.attackDamage
                else:
                    return self.attackDamage * 2
            else: 
                if randomHit == 3: return 0        