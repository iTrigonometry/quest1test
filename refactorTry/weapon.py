
#TODO добавить патроны
#TODO добавить durability прочность
#TODO разработать логику duraility 
class Weapon:

    def __init__(self, name):
        self.name = name
        self.__attackDamage = 0
        self.__criticalChance = 0

#! заморожено на неопределенный срок
        self.__durability = 100
        self.__patron = 0

    def upgrade(self, plusAttack, plusCritChance):
        self.__attackDamage += plusAttack
        self.__criticalChance += plusCritChance

    def getAttackDamage(self):
        return self.__attackDamage
    def setAttackDamage(self, attackDamage):
        self.__attackDamage = attackDamage

    def getCriticalChance(self):
        return self.__criticalChance
    def setCritChance(self, criticalChance):
        self.__criticalChance = criticalChance