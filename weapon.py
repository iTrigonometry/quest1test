
#TODO добавить патроны
#TODO добавить durability прочность
#TODO разработать логику duraility 
class Weapon:

    def __init__(self, name):
        self.name = name
        self.__attackDamage = 0
        self.__critChance = 0


        self.__durability = 100
        self.__patron = 0

    def upgrade(self, plusAttack, plusCritChance):
        self.__attackDamage += plusAttack
        self.__critChance += plusCritChance

    def getAttackDamage(self):
        return self.__attackDamage

    def getCritChance(self):
        return self.__critChance