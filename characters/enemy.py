from characters.character import Character
from random import randint


"""#LIST OF ENEMY

SVYATOY - Святой
ВПЕРВЫЕ ДНИ ШАРАГОПОКАЛИПСИСА РАЗДАВАЛ ВМЕСТЕ
С BAJENOV and MACHADULOOEV СИГАРЕТЫ,
ПОСЛЕ ПРИЧИСЛЕНЫ К ЛИКУ СВЯТЫХ, ДАЮТ
ПАЧКУ МАЛЬБОРО ЗА ВЕРМИШЕЛЬКУ ИЛИ ХЛАДОМАЗЬ

STYRASTA - Староста - Толян - Парикмахер - Алкоголик
ВСЁ ЕЩЕ СТАРОСТА 560 ГРУППЫ, ХОТЯ ПРОШЛО УЖЕ 20 ЛЕТ,
ДАЁТ НЕПОНЯТНЫЕ ЗАДАНИЯ И ПРАКТИЧЕСКИ НЕ ПЛАТИТ,
“НО ОПЫТ, КОТОРЫЙ, ТЫ ПРИОБРЕТАЕШЬ ВО ВРЕМЯ ЗАДАНИЙ
НЕ ИСЧИСЛИТЬ ДЕНЬГАМИ”(C)STYRASTA
"""


class Enemy(Character):
    def __init__(self):
        super().__init__()

    def hit(self):
        number_of_hit = randint(1, 3)
        if number_of_hit == 1:
            return self.get_attack_damage()
        elif number_of_hit == 2:
            random_num = randint(0, 100)
            if random_num >= self.get_critical_chance():
                return self.get_attack_damage()
            else:
                return self.get_attack_damage() * 2
        else:
            return self.get_weapon_hit_damage()

    def set_enemy(self, enemy_name):
        self.set_name(enemy_name)
        self.set_attack_damage(- self.get_attack_damage())
        self.set_HP(- self.get_HP())
        self.set_defence(- self.get_defence())
        self.set_critical_chance(- self.get_critical_chance())
        __name = self.get_name()

        if __name == "SVYATOY":
            self.set_HP(100)
            self.set_attack_damage(1)
            self.set_defence(0)
            self.set_critical_chance(10)

        if __name == "STYROSTA":
            self.set_HP(999)
            self.set_attack_damage(999)
            self.set_defence(100)
            self.set_critical_chance(100)
