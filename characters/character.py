from items.weapon import Weapon
from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self):
        self.__name = "Default Name"
        self.__hp = 100
        self.__attack_damage = 1
        self.___inventory = {}
        self.is_weapon_in_use = False

        self.__amount_of_doshirak = 0
        self.__doshirak_effect = 50
        self.__critical_chance = 0

        self.__defence = 5
        self.__weapon = Weapon("SomeName")

    @abstractmethod
    def hit(self):
        pass

    def use_doshirak(self):
        pass

# !GETERS SETTERS GOVNA
# **Name set get
    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

# ** HP set get
    def get_HP(self):
        return self.__hp

    def set_HP(self, how_much_to_change: int):
        self.__hp += how_much_to_change

# **attackDamage set get
    def get_attack_damage(self):
        return self.__attack_damage

    def set_attack_damage(self, how_much_to_change: int):
        self.__attack_damage += how_much_to_change

# **_inventory
    def get_inventory(self):
        pass

    def set_inventory(self):
        pass

# ** Weapon set get
# ! добавить проверку на текущее оружие
    def get_weapon_name(self):
        if self.__is_weapon_in_use:
            return self.__weapon.get_name()
        else:
            return "У вас нет оружия"

    def set_weapon(
            self, name, attack_damage, crit_chance):
        self.__is_weapon_in_use = True
        self.__weapon.set_name(name)
        self.__weapon.set_attack_damage(attack_damage)
        self.__weapon.set_critical_chance(crit_chance)

    def remove_weapon(self):
        self.__is_weapon_in_use = False
        self.set_weapon("SomeName", 0, 0)

    def get_weapon_hit_damage(self):
        return self.__weapon.get_damage_of_hit()

    # **Doshiraks get set
    def get_amount_of_doshirak(self):
        return self.__amount_of_doshirak

    def set_amount_of_doshirak(self, how_much_to_change):
        self.__amount_of_doshirak += how_much_to_change

# **Defence get set
    def get_defence(self):
        return self.__defence

    def set_defence(self, how_much_to_change):
        self.__defence += how_much_to_change

# **CriticalChance get set
    def set_critical_chance(self, how_much_to_change):
        self.__critical_chance += how_much_to_change

    def get_critical_chance(self):
        return self.__critical_chance
