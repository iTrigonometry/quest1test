def printMsg(message):
    """вывод сообщения. Если вдруг я решусь сделать все в окошках то мне не придется переписывать все
    
    Arguments:
        message {string} -- text of message
    """
    print(message)

def printFightMsg():
    """Метод для выбора действия
    
    Returns:
        int -- action
    """
    print("На выбор у вас есть след позиции:\n1)Удар рукой (наносит ваш обычный урон + шанс крита в 5%)\n2)Удар ногой (есть шанс крита в 25%, но урон меньше)\n3)Использовать оружие (уникальный урон с возможностью прокачки)")
    print("Ну выбирай:")

    x = 0
    while x<1 or x>3:
        try:
            x = int(input())
            return x
        except ValueError:
            print("Ты не справился даже с этим. Пошел нахуй")
            return -1 