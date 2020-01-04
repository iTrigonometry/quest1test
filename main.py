import utils as ut
from player import Player
from enemy import Enemy
import sys
import random
#! важные переменые
#! для врага ВСЕГДА ИСПОЛЬЗОВАТЬ enm
#! Игрок прячется в player


"""
    Готовые TODO
    #TODO сделать показ текущего состояния хп мб дамага на экране и добавить пробелы между блоками сражения

    #TODO поработать над диалогами. Читаются не очень   
            Тотальная переработка сюжета
    #TODO сделать рандомный выбор первого атакующего в начале боя
            #!Вероятно нужны тесты
"""

#TODO урон наносится как float а должен как int Либо оставляю либо нахер
#TODO перенести все начало в отдельный метод main и запускать его через условие if __name__ == __main__


def quest1_Start():
    """Герой заходит в коморку и происходит диалог с STYROSTA
    """
    ut.printMsg("STYROSTA - Привет, " + str(player.name) + "." +
                "Ты уже видился с ILYLBAN? Хотя не важно. У него точно все хорошо.")
    ut.printMsg("STYROSTA - У нас есть проблема")



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


    whoIsFirst = random.randint(1,2) #** 1- player 2- enemy

    def __playerAttack():
        numberOfHit = ut.printFightMsg()
        if numberOfHit == -1: enm.hp -= 0
        else:
            if numberOfHit == 1: enm.hp -= player.hit("hand")
            else:
                if numberOfHit == 2: enm.hp -= player.hit("leg")
                else:
                    if numberOfHit == 3: enm.hp -= player.hit("weapon")
                    else:
                        player.useDoshirak()
        ut.printMsg("ХП противника равно: " + str(enm.hp)) 

    def __enemyAttack():
        ut.printMsg("Атакует противник")
        player.hp -= enm.hit()
        ut.printMsg("Ваше ХП равно: " + str(player.hp) + "\n")


    while player.hp > 0 and enm.hp > 0:
        if whoIsFirst == 1: #**player First
            __playerAttack()
            __enemyAttack()
        else: #**enemy First
            __enemyAttack()
            __playerAttack()


    #** who is win
    if player.hp > 0:
        ut.printMsg("Вы победили " + str(enm.name))
    else:
        ut.printMsg("Вы проиграли. Оставшееся ХП противника: " + str(enm.hp))
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
enm = Enemy()
enm.setEnemy("SVYATOY")

fight()

ut.printMsg("SVYATOY - А ты что-то можешь.")
answer = ut.printQuestionMsg2Option("Тут STYRASTA ищет волантеров. Не хочешь поучавствовать?","Да", "Нет")
if answer == 1:
    ut.printMsg("SVYATOY - Он у себя в коморке")
    ut.printMsg("Вы проходите в коморку.")
else:
    ut.printMsg("SVYATOY - ЛИЧНО МНЕ ПОЕБАТЬ. Пацаны затаскивайте")
    ut.printMsg("Вас насильно затаскивают в коморку где сидит STYRASTA")
ut.printMsg("Там пахнет так себе если честно.\n" +
            "Не тесно, но и не сказать что есть куда яблоку упасть.\n"+
            "КАЗАХСТАН. Первое что приходит вам в голову")

#? перенести в отдельные методы историю или нет?

