from random import randint
#TODO добавить патроны
#TODO добавить durability прочность
#TODO разработать логику duraility

class Weapon:

    def __init__(self, name):
        self.__name = name
        self.__attackDamage = 1
        self.__criticalChance = 0

#! заморожено на неопределенный срок
        self.__durability = 100
        self.__patron = 0

    def upgrade(self, plusAttack, plusCriticalChance):
        self.__attackDamage += plusAttack
        self.__criticalChance += plusCriticalChance

    def getAttackDamage(self):
        return self.__attackDamage
    def setAttackDamage(self, attackDamage):
        self.__attackDamage = attackDamage

    def getCriticalChance(self):
        return self.__criticalChance
    def setCritChance(self, criticalChance):
        self.__criticalChance = criticalChance

    def getName(self):
        return self.__name
    def setName(self, newName):
        self.__name = newName


    def getDamageOfHit(self):
        randomNum = randint(0,100)
        if randomNum >= self.__criticalChance:
            return self.__attackDamage
        else: return self.__attackDamage * 2