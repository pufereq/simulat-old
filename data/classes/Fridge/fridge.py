"""Fridge class."""

from rich.prompt import Prompt
from rich import print

from data.clear import clear


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
        clear()
        print(f'''[bold green]simulat[/bold green]
  [b yellow]contents:[/b yellow]
    {self.fridge_contents()}
  [bold yellow]interactions:[/bold yellow]
    [magenta]eat - eat contents[/magenta]
    [magenta]back - go back to panel[/magenta]
    ''')
        choice = Prompt.ask('Fridge',
                            choices=['eat', 'back'],
                            default='back',
                            show_choices=False)
        if choice == 'eat':
            self.eat_from_fridge()
        elif choice == 'back':
            main_character.check_needs()

    def eat_from_fridge(self):
        """Eat contents from Fridge to raise or decrease needs."""
        from data.game import panel, main_character
        print(f'''[b green]simulat[/b green]
  [b yellow]fridge:[/b yellow]
    [bold cyan]eat raw:[/bold cyan]
      [magenta]bread:[/magenta] [bold italic blue]+8 hunger; -1 fun[/bold italic blue]
      [magenta]vegetables:[/magenta] [bold italic blue]+5 hunger; +2 fun[/bold italic blue]
      [magenta]fruits:[/magenta] [bold italic blue]+7 hunger; +4 fun[/bold italic blue]
      [magenta]eggs:[/magenta] [bold italic blue]+3 hunger; -2 fun[/bold italic blue]
      [magenta]flour:[/magenta] [bold italic blue]+1 hunger; -10 fun; -5 hygiene[/bold italic blue]
      [magenta]meat:[/magenta] [bold italic blue]+6 hunger; -4 fun[/bold italic blue]
        ''')
        choice = Prompt.ask(
            'eat raw',
            choices=['bread', 'vegetables', 'fruits',
                     'eggs', 'flour', 'meat', 'back'],
            show_choices=False,
            default='back')

        if choice == 'bread':
            self.bread -= 1
            main_character.hunger += 8
            main_character.fun -= 1
        elif choice == 'vegetables':
            self.vegetables -= 1
            main_character.hunger += 5
            main_character.fun += 2
        elif choice == 'fruits':
            self.fruits -= 1
            main_character.hunger += 7
            main_character.fun += 4
        elif choice == 'eggs':
            self.eggs -= 1
            main_character.hunger += 3
            main_character.fun -= 2
        elif choice == 'flour':
            self.flour -= 1
            main_character.hunger += 1
            main_character.fun -= 10
            main_character.hygiene -= 5
        elif choice == 'meat':
            self.meat -= 1
            main_character.hunger += 6
            main_character.fun -= 4
        elif choice == 'back':
            panel()
        self.interact()

    def fridge_contents(self):
        """Return fridge contents."""
        return (f'''[magenta]bread:[/magenta] [b i blue]{self.bread}[/b i blue]
    [magenta]vegetables:[/magenta] [b i blue]{self.vegetables}[/b i blue]
    [magenta]fruits:[/magenta] [b i blue]{self.fruits}[/b i blue]
    [magenta]eggs:[/magenta] [b i blue]{self.eggs}[/b i blue]
    [magenta]flour:[/magenta] [b i blue]{self.flour}[/b i blue]
    [magenta]meat:[/magenta] [b i blue]{self.meat}[/b i blue]''')

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
            raise NameError(f'Item {item} not found.')
