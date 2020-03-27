from characters.character import Character
from random import randint
# import utils.utils as ut


class Player(Character):
    def __init__(self):
        super().__init__()

    def hit(self, name_of_hit: str):
        base_critical_chance = self.get_critical_chance()
        random_num = randint(0, 100)
        if name_of_hit == "leg":
            if random_num > base_critical_chance + 10:
                return self.get_attack_damage() - (self.get_attack_damage()/2)
            else:
                return self.get_attack_damage() * 2
        elif name_of_hit == "hand":
            if random_num > base_critical_chance:
                return self.get_attack_damage()
            else:
                return self.get_attack_damage() * 2

        elif name_of_hit == "weapon":
            if self.is_weapon_in_use:
                return self.get_weapon_hit_damage()
            else:
                return 0
        else:
            return 0
