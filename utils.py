from time import sleep

def printMsg(message):
    """вывод сообщения. Если вдруг я решусь сделать все в окошках то мне не придется переписывать все

    Arguments:
        message {string} -- text of message
    """
    __delayBeforeNextMessage()
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

def printQuestionMsg2Option(message, optionOne, optionTwo):
    print(message + "\n1." + optionOne + "\n2." + optionTwo)
    x = 0
    while x<1 or x>2:
        try:
            x = int(input())
            if x<1 or x >2:
                print("А если подумать?")
                continue
            else:
                return x
        except ValueError:
            print("А если подумать?")
            continue

def __delayBeforeNextMessage():
    """Просто задержка между сообщениями,
        чтобы хоть как то успевать следить за тем что происходит
    """
    sleep(1)