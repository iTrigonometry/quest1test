import random
import utils as ut
from weapon import Weapon


"""готовые TODO

    #TODO решить что сделать приватным а что оставить как есть
            Решено что похуй, главное остальное не зафакапить
    #TODO добавить возможность использовать Doshirak
            Теперь его можно использовать. Для того чтобы понять сколько он восстанавливает hp,
            можно посмотреть на значение __doshirakEffect
            #! Есть вероятность постоянного использования и стака большого количества хп
            #! возможно стоит востанавливать только часть хп или сделть ограничение хп в виде __maxHP

    #TODO пересмотреть урон атаки оружием. Потому что что-то имбой попахивает
            Просто добавляем патроны и износ. 


    #TODO добавить новый параметр DEFENCE. Разработать его логику
            Было решено что со 100% вероятностью мы блокируем процент урона который на нас приходится

"""



#TODO сделать инвентарь
#TODO дать возможность просматривать инвентарь



#TODO сделать выброс оружия



class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attackDamage = 1
        self.inventory = {}
        self.__isWeaponInUse = False
        self.weapon = Weapon("SomeName")
        self.__amountOfDoshirak = 0
        self.__doshirakEffect = 50

        self.__defence = 5

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

    def useDoshirak(self):
        self.hp += self.__doshirakEffect



#**Модули DEFENCE
    def getDefence(self):
        return self.__defence
    def upgradeDefence(self, plusDefence):
        self.__defence += plusDefence



#** НЕ ИСПОЛЬЗУЕМЫЕ МЕТОДЫ


    def __useInventory(self):
        #! не используется

        print ("В вашем инвентаре " + len(self.inventory) + "предметов")