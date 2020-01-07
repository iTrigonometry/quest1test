from refactorTry.character import Character
from random import randint

#TODO добавить возможность экипировки оружия
#TODO так как в планах последним боссом сделать STYROSTA, то у него завышеные характеристики, думаю стоит добавить изменение его характеристик по ходу сюжета


"""#LIST OF ENEMY

SVYATOY - Святой
ВПЕРВЫЕ ДНИ ШАРАГОПОКАЛИПСИСА РАЗДАВАЛ ВМЕСТЕ С BAJENOV and MACHADULOOEV СИГАРЕТЫ,
ПОСЛЕ ПРИЧИСЛЕНЫ К ЛИКУ СВЯТЫХ, ДАЮТ ПАЧКУ МАЛЬБОРО ЗА ВЕРМИШЕЛЬКУ ИЛИ ХЛАДОМАЗЬ

STYRASTA - Староста - Толян - Парикмахер - Алкоголик
ВСЁ ЕЩЕ СТАРОСТА 560 ГРУППЫ, ХОТЯ ПРОШЛО УЖЕ 20 ЛЕТ,
ДАЁТ НЕПОНЯТНЫЕ ЗАДАНИЯ И ПРАКТИЧЕСКИ НЕ ПЛАТИТ,
“НО ОПЫТ, КОТОРЫЙ, ТЫ ПРИОБРЕТАЕШЬ ВО ВРЕМЯ ЗАДАНИЙ НЕ ИСЧИСЛИТЬ ДЕНЬГАМИ”(C)STYRASTA
"""



class Enemy(Character):
    def hit(self):
        numberOfHit = randint(1,3)
        if numberOfHit == 1: return self.getAttackDamage()
        elif numberOfHit == 2:
            randomNum = randint(0,100)
            if randomNum >= self.getCriticalChance(): return self.getAttackDamage()
            else: return self.getAttackDamage()*2
        else: return self.weapon.getDamageOfHit()




    def setEnemy(self, enemyName):
        self.setName(enemyName)
        self.setAttackDamage( - self.getAttackDamage())
        self.setHP( - self.getHP())
        self.setDefence( - self.getDefence())
        self.setCriticalChance( - self.getCriticalChance())

        __name = self.getName()

        if __name == "SVYATOY":
            self.setHP(100)
            self.setAttackDamage(1)
            self.setDefence(0)
            self.setCriticalChance(10)

        if __name == "STYROSTA":
            self.setHP(999)
            self.setAttackDamage(999)
            self.setDefence(100)
            self.setCriticalChance(100)
