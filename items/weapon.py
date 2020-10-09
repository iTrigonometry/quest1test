from random import randint


class Weapon:

    def __init__(self, name):
        self.__name = name
        self.__attack_damage = 1
        self.__critical_chance = 0

# ! заморожено на неопределенный срок
        self.__durability = 100
        self.__patron = 0

    def upgrade(self, attack, critical_chance):
        self.__attack_damage += attack
        self.__critical_chance += critical_chance

    def get_attack_damage(self):
        return self.__attack_damage

    def set_attack_damage(self, attack_damage):
        self.__attack_damage = attack_damage

    def get_critical_chance(self):
        return self.__critical_chance

    def set_critical_chance(self, critical_chance):
        self.__critical_chance = critical_chance

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_damage_of_hit(self):
        random_num = randint(0, 100)
        if random_num >= self.__critical_chance:
            return self.__attack_damage
        else:
            return self.__attack_damage * 2
