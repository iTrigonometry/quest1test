import random
import utils as ut
from weapon import Weapon

#TODO сделать инвентарь
#TODO дать возможность просматривать инвентарь
#TODO решить что сделать приватным а что оставить как есть

#! TODO пересмотреть урон атаки оружием. Потому что что-то имбой попахивает

class Player:
    def __init__(self, name):
        self.name = name        
        self.hp = 100
        self.attackDamage = 1
        self.inventory = {}
        self.isWeaponInUse = False
        self.weapon = Weapon("SomeName")

    def setWeapon(self, name):
        """метод установки оружия
        
        Arguments:
            name {[string]} -- [name of weapon]
        """
        self.weapon = Weapon(name)

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
                    if self.isWeaponInUse:
                        randomNum = random.randint(0,100)
                        ut.printMsg("Ваше оружие" + self.weapon.name)
                        if (randomNum >= self.weapon.critChance):
                            return self.attackDamage - self.attackDamage/3
                        else:
                            return self.attackDamage+self.attackDamage/2
                    else:
                        ut.printMsg("У вас нет оружия")
                        return 0

    def __useInventory(self):
        #! не используется
        
        print ("В вашем инвентаре " + len(self.inventory) + "предметов")