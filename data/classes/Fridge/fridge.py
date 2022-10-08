"""Fridge class."""

from rich.prompt import Prompt
from rich import print

from data.utils import print_header


class Fridge():
    """A Fridge class used to store food."""

    def __init__(self, bread, vegetables, fruits, eggs, flour, meat,
                 randomize=False):
        """Initialize Fridge() class.

        Args:
            bread (int): Set amount of bread in Fridge().
            vegetables (int): Set amount of vegetables in Fridge().
            fruits (int): Set amount of fruits in Fridge().
            eggs (int): Set amount of eggs in Fridge().
            flour (int): Set amount of flour in Fridge().
            meat (int): Set amount of meat in Fridge().
            randomize (bool, optional): If randomize above. Defaults to False.
        """
        self.bread = bread
        self.vegetables = vegetables
        self.fruits = fruits
        self.eggs = eggs
        self.flour = flour
        self.meat = meat

    def interact(self):
        """Interact with Fridge. Allows to eat contents."""
        from data.game import main_character
        fridge_contents = self.fridge_contents()
        prompt = print_header("home", [], "fridge",
                              [{'category_name': "contents", 'data':
                               [{'name': "bread", 'desc': fridge_contents['bread'], 'interaction': False},
                                {'name': "vegetables", 'desc': fridge_contents['vegetables'], 'interaction': False},
                                {'name': "fruits", 'desc': fridge_contents['fruits'], 'interaction': False},
                                {'name': "eggs", 'desc': fridge_contents['eggs'], 'interaction': False},
                                {'name': "flour", 'desc': fridge_contents['flour'], 'interaction': False},
                                {'name': "meat", 'desc': fridge_contents['meat'], 'interaction': False}]}],
                              "interactions",
                              [{'category_name': 'use', 'data':
                               [{'name': "eat", 'desc': "eat fridge contents", 'interaction': True}]}],
                              go_back=main_character.check_needs, clear_screen=True)

        if prompt == 'eat':
            self.eat_from_fridge()

    def eat_from_fridge(self):
        """Eat contents from Fridge to raise or decrease needs."""
        from data.game import main_character
        fridge_contents = self.fridge_contents()
        prompt = print_header("home", [], "fridge",
                              [{'category_name': "contents", 'data':
                                [{'name': "bread", 'desc': fridge_contents['bread'], 'interaction': False},
                                 {'name': "vegetables", 'desc': fridge_contents['vegetables'], 'interaction': False},
                                 {'name': "fruits", 'desc': fridge_contents['fruits'], 'interaction': False},
                                 {'name': "eggs", 'desc': fridge_contents['eggs'], 'interaction': False},
                                 {'name': "flour", 'desc': fridge_contents['flour'], 'interaction': False},
                                 {'name': "meat", 'desc': fridge_contents['meat'], 'interaction': False}]},
                               {'category_name': 'details \[to change]', 'data':  # TODO: change category_name to sth more appropriate
                                [{'name': "bread", 'desc': "+8 hunger; -1 fun", 'interaction': False},
                                 {'name': "vegetables", 'desc': "+5 hunger; +2 fun", 'interaction': False},
                                 {'name': "fruits", 'desc': "+7 hunger; +4 fun", 'interaction': False},
                                 {'name': "eggs", 'desc': "+3 hunger; -2 fun", 'interaction': False},
                                 {'name': "flour", 'desc': "+1 hunger; -10 fun; -5 hygiene", 'interaction': False},
                                 {'name': "meat", 'desc': "+6 hunger; -4 fun", 'interaction': False}]}],
                              "interactions",
                              [{'category_name': "eat raw", 'data':
                                [{'name': "bread", 'desc': "eat raw bread", 'interaction': True},
                                 {'name': "vegetables", 'desc': "eat raw vegetables", 'interaction': True},
                                 {'name': "fruits", 'desc': "eat raw fruits", 'interaction': True},
                                 {'name': "eggs", 'desc': "eat raw eggs", 'interaction': True},
                                 {'name': "flour", 'desc': "eat raw flour", 'interaction': True},
                                 {'name': "meat", 'desc': "eat raw meat", 'interaction': True}]}],
                              go_back=self.interact, clear_screen=True)

        if prompt == 'bread':
            self.bread -= 1
            main_character.hunger += 8
            main_character.fun -= 1
        elif prompt == 'vegetables':
            self.vegetables -= 1
            main_character.hunger += 5
            main_character.fun += 2
        elif prompt == 'fruits':
            self.fruits -= 1
            main_character.hunger += 7
            main_character.fun += 4
        elif prompt == 'eggs':
            self.eggs -= 1
            main_character.hunger += 3
            main_character.fun -= 2
        elif prompt == 'flour':
            self.flour -= 1
            main_character.hunger += 1
            main_character.fun -= 10
            main_character.hygiene -= 5
        elif prompt == 'meat':
            self.meat -= 1
            main_character.hunger += 6
            main_character.fun -= 4
        self.interact()

    def fridge_contents(self):
        """Return fridge contents."""
        return {"bread": self.bread, "vegetables": self.vegetables,
                "fruits": self.fruits, "eggs": self.eggs,
                "flour": self.flour, "meat": self.meat}

    def add_to_fridge(self, item, quantity):
        """Add items to the fridge.

        If requested to add a non-exsistent item, raise an error.

        Args:
            item (str): item name
            quantity (int): quantity to add
        """
        if item == 'bread':
            self.bread += quantity
        elif item == 'vegetables':
            self.vegetables += quantity
        elif item == 'fruits':
            self.fruits += quantity
        elif item == 'eggs':
            self.eggs += quantity
        elif item == 'flour':
            self.flour += quantity
        elif item == 'meat':
            self.meat += quantity
        else:
            raise NameError(f"Item {item} not found.")
