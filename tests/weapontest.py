import sys
sys.path.append(sys.path[0][:-6])


from items.weapon import Weapon


weapon = Weapon("SomeName")


print("getName SomeName :::: " + weapon.getName())
weapon.setName("newName")
print("setName newName ::::: " + weapon.getName())





