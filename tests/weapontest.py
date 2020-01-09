import sys
sys.path.append(sys.path[0][:-6])


from items.weapon import Weapon


weapon = Weapon("SomeName")


print("getName SomeName :::: " + weapon.getName())
weapon.setName("newName")
print("setName newName ::::: " + weapon.getName())

print("getAttackDamage 1 ::::::: " + str(weapon.getAttackDamage()))
weapon.setAttackDamage(123)
print("getAttackDamage 123 :::: " + str(weapon.getAttackDamage()))


print("getCriticalChance 0 ::: " + str(weapon.getCriticalChance()))
weapon.setCriticalChance(123)
print("getCriticalChance 123 ::: " + str(weapon.getCriticalChance()))


print("upgrade test +1 +1")
print("attackDamage " + str(weapon.getAttackDamage()))
print("criticalChance " + str(weapon.getCriticalChance()))
weapon.upgrade(1,1)
print("attackDamage " + str(weapon.getAttackDamage()))
print("criticalChance " + str(weapon.getCriticalChance()))


