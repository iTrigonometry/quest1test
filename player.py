import random
import utils as ut
from weapon import Weapon

#TODO сделать инвентарь
#TODO дать возможность просматривать инвентарь
#TODO решить что сделать приватным а что оставить как есть
#TODO добавить возможность использовать Doshirak
#TODO добавить новый параметр DEFENCE. Разработать его логику
#TODO сделать выброс оружия

#! TODO пересмотреть урон атаки оружием. Потому что что-то имбой попахивает

class Player:
    def __init__(self, name):
        self.name = name        
        self.hp = 100
        self.attackDamage = 1
        self.inventory = {}
        self.__isWeaponInUse = False
        self.weapon = Weapon("SomeName")
        self.__amountOfDoshirak = 0

    def setDoshirak(self, numberOfDoshirak):
        """Прибавляет необходимое количество предмета Doshirak
        
        Arguments:
            numberOfDoshirak {int} -- the amount to be added
        """
        self.__amountOfDoshirak += numberOfDoshirak
    
    def getDoshirak(self):
        return self.__amountOfDoshirak

    def setWeapon(self, name):
        """метод установки оружия
        
        Arguments:
            name {[string]} -- [name of weapon]
        """
        self.weapon = Weapon(name)
        self.__isWeaponInUse = True

    def upgradeHit(self, plusAttack):
        self.attackDamage += plusAttack


    def getNameToWeapon(self, nameOfWeapon):
        """ВременноОдноразовый метод. Присваивает имя оружию
        
        Arguments:
            nameOfWeapon {[string]} -- [name of weapon]
        """
        self.weapon.name = nameOfWeapon

    def hit(self, hitName):
        """Метод атаки персонажа выбор зависит от игрока
        
        Arguments:
            hitName {[string]} -- [hand, leg, weapon]
        
        Returns:
            [int] -- [damage]
        """
        if hitName == "leg":
            critChance = 25
            randomNum = random.randint(0,100)
            if (randomNum > critChance):
                return self.attackDamage - (self.attackDamage/2)
            else:
                return self.attackDamage+self.attackDamage
        else:
            if hitName == "hand":
                critChance = 5
                randomNum = random.randint(0,100)
                if (randomNum > critChance):
                    return self.attackDamage
                else:
                    return self.attackDamage+self.attackDamage
            else:
                if hitName == "weapon":
                    if self.__isWeaponInUse:
                        randomNum = random.randint(0,100)
                        ut.printMsg("Ваше оружие" + self.weapon.name)
                        if (randomNum >= self.weapon.getCritChance()):
                            return self.weapon.getAttackDamage() - self.weapon.getAttackDamage()/3
                        else:
                            return self.weapon.getAttackDamage() + self.weapon.getAttackDamage()/2
                    else:
                        ut.printMsg("У вас нет оружия")
                        return 0

    def __useInventory(self):
        #! не используется
        
        print ("В вашем инвентаре " + len(self.inventory) + "предметов")