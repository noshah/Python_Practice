from random import randint

class Die:
    """this class about dice infornation and rolling."""

    def __init__(self, num_sides=8):
        """this method saves number of sides."""
        self.num_sides = num_sides

    def roll(self):
        """this method roll the dice."""
        return randint(1, self.num_sides)
