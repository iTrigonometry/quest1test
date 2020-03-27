from time import sleep


def print_msg(message):
    """вывод сообщения. Если вдруг я решусь сделать
    все в окошках то мне не придется переписывать все

    Arguments:
        message {string} -- text of message
    """
    __delay_before_next_message()
    print(message)


def print_fight_msg():
    """Метод для выбора действия

    Returns:
        int -- action
    """
    print(
            "На выбор у вас есть след позиции:" +
            "\n1)Удар рукой (наносит ваш обычный урон + шанс крита в 5%)" +
            "\n2)Удар ногой (есть шанс крита в 25%, но урон меньше)" +
            "\n3)Использовать оружие (урон который можно прокачать)" +
            "\n4)Использовать доширак(восстанавливает здоровье)")
    print("Ну выбирай:")

    x = 0
    while x < 1 or x > 4:
        try:
            x = int(input())
            if x < 1 or x > 4:
                print_msg("Попробуй еще раз")
            else:
                return x
        except ValueError:
            print("Ты не справился даже с этим. Пошел нахуй")
            return -1


def print_question_msg_2option(message, option1, option2):
    print(message + "\n1." + option1 + "\n2." + option2)
    x = 0
    while x < 1 or x > 2:
        try:
            x = int(input())
            if x < 1 or x > 2:
                print("А если подумать?")
                continue
            else:
                return x
        except ValueError:
            print("А если подумать?")
            continue


def __delay_before_next_message():
    """Просто задержка между сообщениями,
        чтобы хоть как то успевать следить за тем что происходит
    """
    sleep(0)
