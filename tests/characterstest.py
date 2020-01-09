import sys
print(sys.path)
sys.path.append("c:\\Users\\TwentyFiveTons\\Documents\\projects\\quest1test")
#print(sys.path)
from characters.player import Player
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
#   player.setHP(100)
    print("PlayerHP: 100 :::::  " + str(player.getHP()))
    print("Обнуляем")
    player.setHP(- player.getHP())
    print("HP player: 0 :::: " + str(player.getHP()))


    print("проверка модулей HP окончена")
    print()
    print("проверка модулей AttackDamage")

    print("Attack damage default: " + str(player.getAttackDamage()))
    player.setAttackDamage(-199)
    print("attackDamage -199: -198 ::::: " + str(player.getAttackDamage()))

    print("Проверка модулей AttackDamage окончена")
    print()
    print("Проверка модулей weapon")
    print("weapon name is " + player.getWeaponName())
    player.setWeapon("name", 12, 9)
    print("Weapon name is name ::::: " + player.getWeaponName())
    print("Weapon hit damaage is " + str(player.getWeaponHitDamage()))

    print("Проверка модулей weapon окончена")
    print()
    print("Проверка модулей doshirak")
    print("количество doshirak amount( ) :   " + str(player.getAmountOfDoshirak()))
    player.setAmountOfDoshirak(123)
    print("Количество дошираков 123 :::: " + str(player.getAmountOfDoshirak()))

    print("проверка модулей doshirak окончена")
    print()
    print("проверка модулей defence")
    print("defence is 5 ::::: " + str(player.getDefence()))
    player.setDefence(123)
    print("defence is 128 :::::" + str(player.getDefence()))

    print("проверка модулей defence окончена")
    print()
    print("проверка модулей criticalChance")
    print("Critical chance is " + str(player.getCriticalChance()))
    player.setCriticalChance(123)
    print("critical chance is " + str(player.getCriticalChance()))

    print("Проверка модулей critical chance окончена")
    print("Тесты окончены")

player = Player()
enemy = Enemy()

testAllMethodsOfClassCharacter()
