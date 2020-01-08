import sys
print(sys.path)
sys.path.append("c:\\Users\\TwentyFiveTons\\Documents\\projects\\quest1test")
#print(sys.path)
from characters import player
from characters.enemy import Enemy
from items.weapon import Weapon


def testAllMethodsOfClassCharacter():

    print("Проверка модулей NAME")
    player.setName("Test")
    print(player.getName())
    if player.getName() == "Test":
        print("Default Name ::::: " + enemy.getName() + " suka")
        enemy.setName("Sukin sin")
        print(enemy.getName())

    print("Проверка модулей NAME окончена")
    print()
    print("Проверка модулей HP")
    player.setHP(100)
    print("PlayerHP: не помню :::::  " + player.getHP())
    print("Обнуляем")
    player.setHP(- player.getHP())
    print("HP player: 0 :::: " + player.getHP())


    print("проверка модулей HP окончена")
    print()
    print("проверка модулей AttackDamage")


player = player.Player()
enemy = Enemy()

testAllMethodsOfClassCharacter()
