"""
"""
from classes import Dice, Advantage

class Kibble:
    """A series of several checks to craft an item.

    3 Failed rolls in a row leads to failure of the Kibble.
    Tracks information like the total number of rolls, so on.

    Attributes:
        dc: An int to meet or exceed for a roll to "succeed" a single check.
        rolls_needed: An int number of successes to pass
        n_fails: An int number of fails in a row
        n_successes: An int tracking total rolls >= dc
        n_rolls: An int tracking the total checks
    """
    def __init__(self, dc: int, rolls_needed: int):
        self.dc = dc
        self.rolls_needed = rolls_needed

        self.n_fails = 0
        self.n_successes = 0
        self.n_rolls = 0

    def check(self, roll: int):
        """Given a dice check, evaluate success and determine if crafting can continue.

        Args:
            roll: An int to compare to the dc
        
        Returns
            True if crafting can continue and False if it cannot.
        """
        if self.isFailed() or self.isSuccess():
            return False
        self.n_rolls += 1
        if roll >= self.dc:
            self.n_fails = 0
            self.n_successes += 1
            return True
        self.n_fails += 1
        if self.isFailed():
            return False
        return True

    def isSuccess(self):
        return self.n_successes >= self.rolls_needed
    
    def isFailed(self):
        return self.n_fails >= 3

d20 = Dice(20, 5)
tenCheck = Kibble(10, 10)

while not( tenCheck.isSuccess() or tenCheck.isFailed() ):
    input(f"{tenCheck.n_rolls} rolls")
    roll = d20.roll()
    tenCheck.check( roll )
    print(roll)