import utils.utils as ut
from characters.player import Player
from characters.enemy import Enemy
import sys
import random


def quest1_start():
    """Герой заходит в коморку и происходит диалог с STYROSTA
    """
    ut.print_msg(
                "STYROSTA - Привет, " + str(player.get_name()) + "." +
                "Ты уже видился с ILYLBAN? Хотя не важно." +
                "У него точно все хорошо.")
    ut.print_msg("STYROSTA - У нас есть проблема")


def fight():
    ut.print_msg("Бой начался")
    ut.print_msg(
        "Ваше хп равно: " + str(player.get_HP())
        + "\nХП противника равно: " + str(enm.get_HP()))

    who_is_first = random.randint(1, 2)  # ** 1- player 2- enemy

    def __player_attack():
        number_of_hit = ut.print_fight_msg()

        if number_of_hit == -1:
            enm.set_HP(-0)
        elif number_of_hit == 1:
            __player_hand_hit = player.hit("hand")
            enm.set_HP(
                - __player_hand_hit -
                (__player_hand_hit * enm.get_defence() / 100))
        elif number_of_hit == 2:
            __player_leg_hit = player.hit("leg")
            enm.set_HP(
                - __player_leg_hit -
                (__player_leg_hit * enm.get_defence() / 100))
        elif number_of_hit == 3:
            __player_weapon_hit = player.hit("weapon")
            enm.set_HP(
                    -__player_weapon_hit -
                    (__player_weapon_hit * enm.get_defence() / 100))
        else:
            player.use_doshirak()

        ut.print_msg("ХП противника равно: " + str(enm.get_HP()))

    def __enemy_attack():
        ut.print_msg("Атакует противник")
        __enemyHit = enm.hit()
        player.set_HP(- __enemyHit - (__enemyHit * player.get_defence() / 100))
        ut.print_msg("Ваше ХП равно: " + str(player.get_HP()) + "\n")

    while player.get_HP() > 0 and enm.get_HP() > 0:
        if who_is_first == 1:  # **player First
            __player_attack()
            __enemy_attack()
        else:  # **enemy First
            __enemy_attack()
            __player_attack()

    # ** who is win
    if player.get_HP() > 0:
        ut.print_msg("Вы победили " + str(enm.get_name()))
    else:
        ut.print_msg(
            "Вы проиграли. Оставшееся ХП противника: "
            + str(enm.get_HP()))
        sys.exit(0)


player = Player()
enm = Enemy()
if __name__ == "__main__":
    # СТАРТ КВЕСТА
    ut.print_msg("НАЧАЛО")
    ut.print_msg("И нахера ты это запустил дебил")
    ut.print_msg(
                "Давай так. Тебе уже 22 года. На дворе 2037 год." +
                "Ничего особенного не произошло\nКроме взрыва шараги "
                "и разъеба всего Питера.")
    ut.print_msg(
                "Стураста как всегда не сидит на месте и ищет" +
                "приключений на свою жопу. Ему нужны сталкеры...")
    # КВЕСТ 1
    ut.print_msg("Квест 1. ВОЗВРАЩЕНИЕ НА ПОВЕРХНОСТЬ")
    ut.print_msg("Тебя встречает Святой")
    ut.print_msg("SVYATOY - Слышь ты кто?")
    ut.print_msg("")
    name_of_player = str(input(" О, тебе позволили выбрать имя:"))

    player.set_name(name_of_player)

    ut.print_msg(
            "SVYATOY - Хорошо, " + player.get_name() + ". Защищайся!!!!!!")
    ut.print_msg("Это обучающий бой. И ты точно проиграешь")

    # характеристики врага можно посмотреть в enemy.py.set_enemy()
    enm.set_enemy("SVYATOY")

    fight()

    ut.print_msg("SVYATOY - А ты что-то можешь.")
    answer = ut.print_question_msg_2option(
                    "Тут STYRASTA ищет волантеров." +
                    "Не хочешь поучавствовать?", "Да", "Нет")
    if answer == 1:
        ut.print_msg("SVYATOY - Он у себя в коморке")
        ut.print_msg("Вы проходите в коморку.")
    else:
        ut.print_msg("SVYATOY - ЛИЧНО МНЕ ПОЕБАТЬ. Пацаны затаскивайте")
        ut.print_msg("Вас насильно затаскивают в коморку где сидит STYRASTA")
    ut.print_msg(
                "Там пахнет так себе если честно.\n" +
                "Не тесно, но и не сказать что есть куда яблоку упасть.\n" +
                "КАЗАХСТАН. Первое что приходит вам в голову")

    # ? перенести в отдельные методы историю или нет?
