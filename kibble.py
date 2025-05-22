"""Represents a Kibble's 5e crafting series

Usage example:

    helmet = Kibble(15,3)
    while not(helmet.is_success() or helmet.is_failed()):
        helmet.check(20) # would use a Dice.roll()

"""


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
        name: An str name for the item being crafted
        always_complete: A bool if set True means that any check resulting
            in incrementing n_fails to 3 auto succeeds.
        n_auto_success: An int tracking times auto_complete caused a success
    """
    def __init__(self,
                 dc: int,
                 rolls_needed: int,
                 name: str = "",
                 always_complete: bool = False
                 ):
        self.dc = dc
        self.rolls_needed = rolls_needed
        self.name = name
        self.always_complete = always_complete

        self.n_fails = 0
        self.n_successes = 0
        self.n_rolls = 0
        self.n_auto_successes = 0

    def check(self, roll: int):
        """Given a dice check, evaluate success and determine if crafting can continue.

        Args:
            roll: An int to compare to the dc

        Returns
            True if crafting can continue and False if it cannot.
        """
        if self.always_complete and self.n_fails >= 2:
            self.n_fails = 0
            self.n_successes += 1
            self.n_auto_successes += 1
            return True
        if self.is_failed() or self.is_success():
            return False
        self.n_rolls += 1
        if roll >= self.dc:
            self.n_fails = 0
            self.n_successes += 1
            return True
        self.n_fails += 1
        if self.is_failed():
            return False
        return True

    def is_success(self):
        """Is the crafting a success?

        Returns:
            True if the number of successful checks has surpassed the required amount
        """
        return self.n_successes >= self.rolls_needed

    def is_failed(self):
        """Is the crafting a failure?

        Returns:
            True if the number of failed checks has surpassed 3
        """
        return self.n_fails >= 3

def roll_until_complete( kibble: Kibble, generator = None ):
    """Perform checks on a kibble until it is done.

    Args:
        kibble: A Kibble to repeatedly do check() on
        generator: A function that will provide the number passed to check
            e.g. randint() or Dice.roll()
    """
    if generator is None:
        raise Exception("Generator cannot be None")

    while not( kibble.is_failed() or kibble.is_success() ):
        kibble.check( generator() )
