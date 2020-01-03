from player import Player
from enemy import Enemy
import utils as ut
import sys
def fight():
    """
    Метод для проведения боя
    Сначала бьет игрок потом враг
    #! Тесты
    #! Возможность драки - +
    #! Победа - +
    #! Поражение - +
    #! Неверный ввод - +
    Для тестов необходимы следующие переменные
    enm: Enemy - враг
    player: Player - игрок
    """
    ut.printMsg("Бой начался")
    ut.printMsg("Ваше хп равно: " + str(player.hp) + "\nХП противника равно: " + str(enm.hp))
    while player.hp > 0 and enm.hp > 0:
        numberOfHit = ut.printFightMsg()
        if numberOfHit == -1: enm.hp -=0
        else:
            if numberOfHit == 1: enm.hp -= player.hit("hand")
            else:
                if numberOfHit == 2: enm.hp -= player.hit("leg")
                else:
                    enm.hp -= player.hit("weapon")
        ut.printMsg("ХП противника равно: " + str(enm.hp))
        player.hp -= enm.hit()
        ut.printMsg("Ваше ХП равно: " + str(player.hp) + "\n")
    if player.hp > 0:
        ut.printMsg("Вы победили " + str(enm.name))
    else:
        ut.printMsg("Вы проиграли. Оставшееся ХП противника: " + str(enm.hp))
        sys.exit(0)

enm = Enemy("SVYATOY")
player = Player("123")

fight()

