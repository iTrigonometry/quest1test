import random

"""
    Готовые TODO
    #TODO характеристики в зависимости от врага
            Враги будут добавляться по ходу написания сюжета
    #TODO Упростить создание нового врага
            Теперь вместо переопределения переменной мы просто используем SetEnemy(name)


    #TODO добавить новый параметр DEFENCE. Разработать его логику
            Было решено что со 100% вероятностью мы блокируем процент урона который на нас приходится
"""

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
#класс врага
class Enemy:


    def setEnemy(self, name):
        """Переопределение врага по имени. Имя равно характеристики врага

        Arguments:
            name {str} -- name of Enemy. List of Enemy in enemy.py
        """
        self.name = name

        if self.name == "SVYATOY":
            self.hp = 100
            self.attackDamage = 1
            self.critChance = 10
            self.__defence = 0
        if self.name == "STYRASTA":
            self.hp = 999
            self.attackDamage = 999
            self.critChance = 75
            self.__defence = 0

    def __init__(self):
        self.name = ""
        self.hp = 100
        self.attackDamage = 1
        self.critChance = 10
        self.__defence = 0


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
                if randomNum >= self.critChance: return self.attackDamage
                else:
                    return self.attackDamage * 2
            else:
                if randomHit == 3: return 0


#**Методы DEFENCE
    def getDefence(self):
        return self.__defence
    def upgradeDefence(self, plusDefence):
        self.__defence += plusDefence
