from items.weapon import Weapon
from abc import ABC, abstractmethod

#TODO в getweaponname добавить проверку на установленное оружие

#TODO подумать над использованем доширака
#**     Первый вариант хилит на определенное количество хп
#**     Второй вариант хилит от 1 до 50
#**     Третий варииант от -25 до 50 или что-то вроде того


class Character(ABC):

    def __init__(self):
        self.__name = ""
        self.__hp = 100
        self.__attackDamage = 1
        self.__inventory = {}
        self.isWeaponInUse = False
        self.__weapon = Weapon("SomeName")
        self.__amountOfDoshirak = 0
        self.__doshirakEffect = 50
        self.__criticalChance = 0

        self.__defence = 5

        self.weapon = Weapon("NoName")





    @abstractmethod
    def hit(self):
        pass

    def useDoshirak(self):
        pass




#!GETERS SETTERS GOVNA
#**Name set get
    def getName(self):
        return self.__name
    def setName(self, name: str):
        self.__name = name

#** HP set get
    def getHP(self):
        return self.__hp
    def setHP(self, howMuchToChange: int):
        self.__hp += howMuchToChange

#**attackDamage set get
    def getAttackDamage(self):
        return self.__attackDamage
    def setAttackDamage(self, howMuchToChange: int):
        self.__attackDamage += howMuchToChange

#**Inventory
    def getInventory(self):
        pass
    def setInventory(self):
        pass

#** Weapon set get
#! добавить проверку на текущее оружие
    def getWeaponName(self):
        return self.__weapon.name
    def setWeapon(self, nameOfWeapon, attackDamageOfWeapon, critChanceOfWeapon):
        self.__isWeaponInUse = True
        self.__weapon.name = nameOfWeapon
        self.__weapon.setAttackDamage(attackDamageOfWeapon)
        self.__weapon.setCritChance(critChanceOfWeapon)
    def removeWeapon(self):
        self.__isWeaponInUse = False


#**Doshiraks get set

    def getAmountOfDoshirak(self):
        return self.__amountOfDoshirak()

    def setAmountOfDoshirak(self, howMuchToChange):
        self.__amountOfDoshirak += howMuchToChange


#**Defence get set

    def getDefence(self):
        return self.__defence
    def setDefence(self, howMuchToChange):
        self.__defence += howMuchToChange

#**CriticalChance get set
    def setCriticalChance(self, howMuchToChange):
        self.__criticalChance += howMuchToChange
    def getCriticalChance(self):
        return self.__criticalChance