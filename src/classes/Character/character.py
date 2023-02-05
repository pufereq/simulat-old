"""Character class."""

from data.res.random_data import random_deplete, random_money
from data.utils import error_handler


class Character():
    """A character class used for main character."""

    @error_handler
    def __init__(self, first_name, last_name, gender, bio):
        """Initialize Character class.

        Args:
            first_name (str): First name
            last_name (str): Last name
            gender (str): Character gender
            bio (str): Biography
        """
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.bio = bio

        # define needs
        self.bladder = 100
        self.hunger = 100
        self.energy = 100
        self.fun = 100
        self.social = 100
        self.hygiene = 100
        self.money = random_money()

    @error_handler
    def deplete_needs(self):
        """Lower needs by random value (0,3)."""
        self.bladder -= random_deplete()
        self.hunger -= random_deplete()
        self.energy -= random_deplete()
        self.fun -= random_deplete()
        self.social -= random_deplete()
        self.hygiene -= random_deplete()

        self.check_needs()

    @error_handler
    def check_needs(self):
        """Check if needs exceed values from 0 to 100 and cap them."""
        from data.game import panel
        if self.bladder < 0:
            self.bladder = 0
        elif self.bladder > 100:
            self.bladder = 100

        if self.hunger < 0:
            self.hunger = 0
        elif self.hunger > 100:
            self.hunger = 100

        if self.energy < 0:
            self.energy = 0
        elif self.energy > 100:
            self.energy = 100

        if self.fun < 0:
            self.fun = 0
        elif self.fun > 100:
            self.fun = 100

        if self.social < 0:
            self.social = 0
        elif self.social > 100:
            self.social = 100

        if self.hygiene < 0:
            self.hygiene = 0
        elif self.hygiene > 100:
            self.hygiene = 100
        panel()
