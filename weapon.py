class Weapon:
    
    def __init__(self, name):
        self.name = name
        self.attackDamage = 0
        self.critChance = 0
    
    def upgrade(self, plusAttack, plusCritChance):
        self.attackDamage += plusAttack
        self.critChance += plusCritChance