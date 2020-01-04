from weapon import Weapon
from abc import ABC, abstractmethod
#TODO в getweaponname добавить проверку на установленное оружие

class Character(ABC):

    def __init__(self):
        self.__name = ""
        self.__hp = 100
        self.__attackDamage = 1
        self.__inventory = {}
        self.__isWeaponInUse = False
        self.__weapon = Weapon("SomeName")
        self.__amountOfDoshirak = 0
        self.__doshirakEffect = 50

        self.__defence = 5





    @abstractmethod
    def hit(self):
        pass






#!GETERS SETTERS GOVNA
#**Name set get
    def getName(self):
        return self.__name
    def setName(self, name: str):
        self.name = name

#** HP set get
    def getHP(self):
        return self.__hp
    def setHP(self, howMuchToChange):
        self.__hp += howMuchToChange

#**attackDamage set get
    def getAttackDamage(self):
        return self.__attackDamage
    def setAttackDamage(self, howMuchToChange):
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
        self.__weapon.name = nameOfWeapon
        self.__weapon.setAttackDamage(attackDamageOfWeapon)
        self.__weapon.setCritChance(critChanceOfWeapon)

#**Doshiraks get set

    def getAmountOfDoshirak(self):
        return self.__amountOfDoshirak()

    def setAmountOfDoshirak(self, howMuchToChange):
        self.__amountOfDoshirak += howMuchToChange

