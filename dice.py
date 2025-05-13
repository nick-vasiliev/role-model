"""Contains classes for modelling dice rolls.

Dice represents a dN dice that can be rolled with modifiers.
Advantage is an enum to represent rolling a Dice and 
    taking the Max or Min roll when many dice are rolled.

Usage example:

    hit = Dice(20)
    damage = Dice(6,3)
    if hit.roll() >= 11:
        print(damage.roll())

"""
from random import randint
from enum import Enum


class Advantage(Enum):
    """Enum for advantage/disadvantage or nothing
    """
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
            advantage: An Advantage enum that allows taking
                the max or min dice when amount >1.
            amount: An int that specifies the number of dice to roll.
                Will take the average if there is no Advantage specified.
        
        Returns:
            An int which is the average roll when no advantage, max
                roll when advantage, and min roll with disadvantage.
        """
        current = randint(1,self.sides)+self.modifier
        for roll_n in range(1,amount):
            next_roll = randint(1,self.sides)+self.modifier
            if advantage == Advantage.DISADVANTAGE:
                current = min(next_roll, current)
            if advantage == Advantage.ADVANTAGE:
                current = max(next_roll, current)
            if advantage == Advantage.NONE:
                # undo last average then average
                current = (current * roll_n + next_roll) / (roll_n + 1)
        return int(current)
