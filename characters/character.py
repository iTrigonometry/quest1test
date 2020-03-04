from items.weapon import Weapon
from abc import ABC, abstractmethod

"""готовые TODO
    # TODO в getweaponname добавить проверку на установленное оружие
        помимо getWeaponName эту проверку добавил в GetWeaponHitDamage
        при запросе имени если оружия нет то возвращается у вас нет оружия
        а при попытке получить урон оружия
            при его несуществовании вы получите 0

    # TODO переписать WEAPONS GET SET
        не помню че там надо было переписать если честно KEKW
"""

# TODO подумать над использованем доширака
# **     Первый вариант хилит на определенное количество хп
# **     Второй вариант хилит от 1 до 50
# **     Третий варииант от -25 до 50 или что-то вроде того


class Character(ABC):

    def __init__(self):
        self.__name = "Default Name"
        self.__hp = 100
        self.__attackDamage = 1
        self.__inventory = {}
        self.isWeaponInUse = False

        self.__amountOfDoshirak = 0
        self.__doshirakEffect = 50
        self.__criticalChance = 0

        self.__defence = 5
        self.__weapon = Weapon("SomeName")

    @abstractmethod
    def hit(self):
        pass

    def useDoshirak(self):
        pass

# !GETERS SETTERS GOVNA
# **Name set get
    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name

# ** HP set get
    def getHP(self):
        return self.__hp

    def setHP(self, howMuchToChange: int):
        self.__hp += howMuchToChange

# **attackDamage set get
    def getAttackDamage(self):
        return self.__attackDamage

    def setAttackDamage(self, howMuchToChange: int):
        self.__attackDamage += howMuchToChange

# **Inventory
    def getInventory(self):
        pass

    def setInventory(self):
        pass

# ** Weapon set get
# ! добавить проверку на текущее оружие
    def getWeaponName(self):
        if self.__isWeaponInUse:
            return self.__weapon.getName()
        else:
            return "У вас нет оружия"

    def setWeapon(
            self, nameOfWeapon, attackDamageOfWeapon, critChanceOfWeapon):
        self.__isWeaponInUse = True
        self.__weapon.setName(nameOfWeapon)
        self.__weapon.setAttackDamage(attackDamageOfWeapon)
        self.__weapon.setCriticalChance(critChanceOfWeapon)

    def removeWeapon(self):
        self.__isWeaponInUse = False
        self.setWeapon("SomeName", 0, 0)

    def getWeaponHitDamage(self):
        if self.__isWeaponInUse:
            return self.__weapon.getDamageOfHit()
        else:
            return 0

    # **Doshiraks get set
    def getAmountOfDoshirak(self):
        return self.__amountOfDoshirak

    def setAmountOfDoshirak(self, howMuchToChange):
        self.__amountOfDoshirak += howMuchToChange

# **Defence get set
    def getDefence(self):
        return self.__defence

    def setDefence(self, howMuchToChange):
        self.__defence += howMuchToChange

# **CriticalChance get set
    def setCriticalChance(self, howMuchToChange):
        self.__criticalChance += howMuchToChange

    def getCriticalChance(self):
        return self.__criticalChance
