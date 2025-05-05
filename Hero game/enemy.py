import entity
import random
"""
Inherits from entity
attributes : 
def __init__ = creates list of enemy names
inherits from super class
def attack = creating a random int for our damage and also makes entity take damage
"""
class Enemy(entity.Entity):
    def __init__(self):
        names = ["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie"]
        super().__init__(name = random.choice(names) , max_hp = random.randint(4, 8))
    #creates its own attack 
    def attack(self, entity):
        dmg = random.randint(1,4)
        entity.take_damage(dmg)
        return f"{self._name} attacks {entity._name} for {dmg} damage!"
    
    