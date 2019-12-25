import utils as ut
from player import Player
from enemy import Enemy
import sys
#! важные переменые
#! для врага ВСЕГДА ИСПОЛЬЗОВАТЬ enm 
#! Игрок прячется в player




#TODO сделать рандомный выбор первого атакующего в начале боя
#TODO сделать показ текущего состояния хп мб дамага на экране и добавить пробелы между блоками сражения
def fight():
    """
    Метод для проведения боя
    Сначала бьет игрок потом враг
    #! на тесты
    #! Возможность драки - +
    #! Победа - 1

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
        ut.printMsg("Вы проиграли: " + str(enm.hp))
        sys.exit(0)
# СТАРТ КВЕСТА
ut.printMsg("НАЧАЛО")
ut.printMsg("И нахера ты это запустил дебил")
ut.printMsg("Давай так. Тебе уже 22 года. На дворе 2037 год. Ничего особенного не произошло\nКроме взрыва шараги и разъеба всего Питера.")
ut.printMsg("Стураста как всегда не сидит на месте и ищет приключений на свою жопу. Ему нужны сталкеры...")
# КВЕСТ 1
ut.printMsg("Квест 1. ВОЗВРАЩЕНИЕ НА ПОВЕРХНОСТЬ")
ut.printMsg("Тебя встречает Святой")
ut.printMsg("SVYATOY - Слышь ты кто?")
ut.printMsg("О, тебе позволили выбрать имя:")
nameOfPlayer = str(input())

player = Player(nameOfPlayer)

ut.printMsg("SVYATOY - Хорошо, " + player.name + ". Защищайся!!!!!!")
ut.printMsg("Это обучающий бой. И ты точно проиграешь")

#характеристики врага можно посмотреть в player.py.setEnemy()
enm = Enemy("SVYATOY")
enm.setEnemy()
print(enm.hp)
fight()



