"""Contains classes for modelling dice rolls.

Leave one blank line.  The rest of this docstring should contain an TODO
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.function_bar()

"""

from random import randint
from enum import Enum

class Advantage(Enum):
    NONE=0
    DISADVANTAGE=1
    ADVANTAGE=2

class Dice:
    """Represents a dN dice.

    Attributes:
        sides: An integer with the number of sides the dice has.
        modifier: An integer that is added to any roll the dice makes.
    """
    def __init__(self, sides: int, modifier: int = 0):
        self.sides = sides
        self.modifier = modifier

    def roll(self, 
             advantage: Advantage = Advantage.NONE, 
             amount: int = 1
             ):
        """ Roll Dice and apply advantages or disadvantages.

        Args:
            advantage: An Advantage enum that allows taking the max or min dice when amount >1.
            amount: An int that specifies the number of dice to roll. Will take the average if there is no Advantage specified.
        """
        current = randint(1,self.sides)+self.modifier
        for roll_n in range(1,amount):
            next = randint(1,self.sides)+self.modifier
            if advantage == Advantage.DISADVANTAGE:
                current = min(next, current)
            if advantage == Advantage.ADVANTAGE:
                current = max(next, current)
            if advantage == Advantage.NONE:
                current = (current * roll_n + next) / (roll_n + 1) # undo last average then average
        return int(current)

n = Dice(20)
print(n.roll(advantage=Advantage.ADVANTAGE, amount=2))