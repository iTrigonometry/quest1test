import quest1test.characters.player
from characters.enemy import Enemy
from items.weapon import Weapon


def testAllMethodsOfClassCharacter():
    player.setName("Test")
    if player.getName() == "Test":
        print(enemy.getName())

player = player.Player()
enemy = Enemy()

testAllMethodsOfClassCharacter()
