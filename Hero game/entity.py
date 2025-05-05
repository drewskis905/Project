import abc
class Entity(abc.ABC):
    """
    Represents a character
    Attributes:
    name : str
    max_hp : int
    """
    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    #entity givens a dmg then takes health away from the max_hp
    def take_damage(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
    
    #getter for hp
    @property
    def hp(self):
        return self._hp
    
    #getter for name
    @property
    def name(self):
        return self._name
    
    
    def heal(self):
        self._hp = self._max_hp
    
    def __str__(self):
        return f"{self._name}\nHP: {self._hp}/{self._max_hp}"
    
    @abc.abstractmethod
    def attack(self, entity):
        pass