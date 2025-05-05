import random
import entity
'''Class handling our hero. Inherits from entity
   Attributes:
   25 : max help of hero
   _loc : starting location of the hero'''
class Hero(entity.Entity):
    def __init__(self, name):
        super().__init__(name, 25)
        self._loc = [0,0] #setting our starting location to 0,0

    def attack(self,entity): 
        '''creating attack for our hero '''
        damage = random.randint(2,5) #allowing damage to be a random int from 2-5
        entity.take_damage(damage)
        return f"{self._name} attacks a {entity._name} for {damage} damage."
    

    '''Creating movement for our character
    first checking if the location is out of bounds, then if not incrementing the player depending on direction'''
    def go_north(self):
        if self._loc[0] - 1 < 0:
            return 'o'
        else:
            self._loc[0] -= 1
            return self._loc
    
    def go_south(self):
        if self._loc[0] + 1 > 4:
            return 'o'
        else:
            self._loc[0] += 1
            return self._loc
    
    def go_east(self):
        if self._loc[1] + 1 > 4:
            return 'o'
        else:
            self._loc[1] += 1
            return self._loc

    def go_west(self):
        if self._loc[1] - 1 < 0:
            return 'o'
        else:
            self._loc[1] -= 1
            return self._loc
    
    @property
    def loc(self):
        return self._loc

        
