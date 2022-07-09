#!/usr/bin/env python3
"""Main game.

Returns:
    None
"""
# game

# imports
import time

from rich import print
from rich.progress import track
from rich.prompt import Prompt, IntPrompt, Confirm

from checks.os_check import clear
from txt.data import (random_first, random_fridge, random_gender,
                      random_last, random_deplete, random_money,
                      get_work_data, random_rob)


class Character():
    """A character class used for main character."""

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

    def deplete_needs(self):
        """Lower needs by random value (0,3)."""
        self.bladder -= random_deplete()
        self.hunger -= random_deplete()
        self.energy -= random_deplete()
        self.fun -= random_deplete()
        self.social -= random_deplete()
        self.hygiene -= random_deplete()

        self.check_needs()

    def check_needs(self):
        """Check if needs exceed values from 0 to 100 and cap them."""
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
            self.social = 0
        elif self.social > 100:
            self.social = 100


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
            randomize (bool, optional): _description_. Defaults to False.
        """
        self.bread = bread
        self.vegetables = vegetables
        self.fruits = fruits
        self.eggs = eggs
        self.flour = flour
        self.meat = meat

    def interact(self):
        """Interact with Fridge. Allows to eat contents."""
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
            choices=['bread',
                     'vegetables',
                     'fruits',
                     'eggs',
                     'flour',
                     'meat',
                     'back'],
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
        return(f'''[magenta]bread:[/magenta] [b i blue]{self.bread}[/b i blue]
    [magenta]vegetables:[/magenta] [b i blue]{self.vegetables}[/b i blue]
    [magenta]fruits:[/magenta] [b i blue]{self.fruits}[/b i blue]
    [magenta]eggs:[/magenta] [b i blue]{self.eggs}[/b i blue]
    [magenta]flour:[/magenta] [b i blue]{self.flour}[/b i blue]
    [magenta]meat:[/magenta] [b i blue]{self.meat}[/b i blue]''')

    def add_to_fridge(self, item, quantity):
        """Add items to the fridge.

        If requested to add a non-exsistent item, raise an error.

        Args:
            item (str): _description_
            quantity (int): _description_
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


class Work():
    """A work class, can add or take money."""

    def __init__(self):
        """Initializates work, currently does nothing."""
        # self.workplace = None
        pass

    def menu(self):
        """Work menu, can pick different jobs."""
        clear()
        print(f'''[b green]simulat[/b green]
    [red]work:[/red]
        [b yellow]menu:[/b yellow]
        [magenta]newspaper[/magenta] - [white]deliver newspapers ($15 / takes 9 seconds)[/white]
        [magenta]pizza[/magenta] - [white]deliver pizzas ($20 / takes 10 seconds)[/white]
        [magenta]office[/magenta] - [white]work at an office ($40 / takes 19 seconds)[/white]
        [magenta]rob[/magenta] - [white]rob people (may earn up to $1000 (risky!))[/white]
        ''')
        choice = Prompt.ask('work',
                            choices=['newspaper',
                                     'pizza',
                                     'office',
                                     'rob',
                                     'back'],
                            default='back',
                            show_choices=False)
        if choice == 'back':
            panel()
        elif choice == 'rob':
            self.rob()
        else:
            self.work(choice)

    def work(self, workplace):
        """Use rich's track to 'visualize' work progress.

        Args:
            workplace (str): Used in defining work time and pay.
        """
        clear()
        work_data = get_work_data(workplace)
        work_time = work_data['time']
        work_pay = work_data['pay']
        try:
            for i in track(range(work_time * 100),
                           description=f'[i yellow]working... ({workplace})'):
                time.sleep(0.01)
        except KeyboardInterrupt:
            print('aborted')
        main_character.money += work_pay
        print(f'[i yellow]you now have {main_character.money}.')
        time.sleep(2)
        self.menu()

    def rob(self):
        """Use rich's track to 'visualize' robbing progess."""
        clear()
        rob_data = random_rob()
        try:
            for i in track(range(rob_data['rob_time'] * 100),
                           description=f'[i yellow]roaming the streets...'):
                time.sleep(0.01)
        except KeyboardInterrupt:
            print('aborted')

        if rob_data['got_caught']:
            if rob_data['money'] == 0:
                print('[i yellow]you have lost all of your stolen money while running away from the police')
                self.menu()

            print(f'[i yellow]police has caught you! you have to pay a [b red]${rob_data["money"]}[/b red] fine.')
            main_character.money -= rob_data['money']
        else:
            if rob_data['money'] == 0:
                print('[i yellow]you have bumped into a stranger and lost your money')
                self.menu()

            print(f'[i yellow]you have stolen [b red]${rob_data["money"]}')
            main_character.money += rob_data['money']
        print(f'[i yellow]you now have ${main_character.money}.')
        time.sleep(2)
        self.menu()


def new_game(debug=False):
    """Start a new game.

    User can choose character details.
    Initializes Character, Fridge and Work classes.

    Args:
        debug (bool, optional): Quick start,
        sets every detail to 'DEBUG'. Defaults to False.
    """
    global main_character
    global home_fridge
    global work
    if debug:
        main_character = Character('DEBUG', 'DEBUG', 'DEBUG', 'DEBUG')
        home_fridge = Fridge(10, 10, 10, 10, 10, 10)
        work = Work()
        panel()
    else:
        clear()
        print('[bold green]Create a new simulat[/bold green]')
        first_name = Prompt.ask('[magenta]First name[/magenta]',
                                default=random_first())
        last_name = Prompt.ask('[magenta]Last name[/magenta]',
                               default=random_last())
        gender = Prompt.ask('[magenta]Gender[/magenta]',
                            default=random_gender())
        bio = Prompt.ask('[magenta]Biography[/magenta]',
                         default='None')
        if bio == 'None':
            bio = None

        main_character = Character(first_name, last_name, gender, bio)
        home_fridge = Fridge(random_fridge(), random_fridge(), random_fridge(),
                             random_fridge(), random_fridge(), random_fridge())
        work = Work()
        panel()


def grocery_store():
    """Buy foodstuffs."""
    clear()
    print(f'''[b green]simulat[/b green]
  [red]grocery store:[/red]
   [b yellow]fridge contents:[/b yellow]
      {home_fridge.fridge_contents()}
   [b yellow]buy:[/b yellow]
      [magenta]bread:[/magenta] [b i blue]$3[/b i blue]
      [magenta]vegetables:[/magenta] [b i blue]$2[/b i blue]
      [magenta]fruits:[/magenta] [b i blue]$2[/b i blue]
      [magenta]eggs:[/magenta] [b i blue]$4[/b i blue]
      [magenta]flour:[/magenta] [b i blue]$1[/b i blue]
      [magenta]meat:[/magenta] [b i blue]$6[/b i blue]
   [b yellow]interactions:[/b yellow]
      [b cyan]buy:[/b cyan]
        [magenta]bread[/magenta] - [white]buy bread[/white]
        [magenta]vegetables[/magenta] - [white]buy vegetables[/white]
        [magenta]fruits[/magenta] - [white]buy fruits[/white]
        [magenta]eggs[/magenta] - [white]buy eggs[/white]
        [magenta]flour[/magenta] - [white]buy flour[/white]
        [magenta]meat[/magenta] - [white]buy meat[/white]

        [magenta]back[/magenta] - [white]back to panel[/white]''')
    choice = Prompt.ask('grocery store',
                        choices=['bread',
                                 'vegetables',
                                 'fruits',
                                 'eggs',
                                 'flour',
                                 'meat',
                                 'back'],
                        default='back',
                        show_choices=False)
    if choice == 'back':
        panel()

    quantity = IntPrompt.ask('quantity')
    if choice == 'bread':
        home_fridge.add_to_fridge('bread', quantity)

    elif choice == 'vegetables':
        home_fridge.add_to_fridge('vegetables', quantity)

    elif choice == 'fruits':
        home_fridge.add_to_fridge('fruits', quantity)

    elif choice == 'eggs':
        home_fridge.add_to_fridge('eggs', quantity)

    elif choice == 'flour':
        home_fridge.add_to_fridge('flour', quantity)

    elif choice == 'meat':
        home_fridge.add_to_fridge('meat', quantity)
    grocery_store()


def panel():
    """Game panel.

    Shows data, allows to interact with game.
    """
    clear()
    print(f'''[b green]simulat[/b green]
  [red]panel:[/red]
    [b yellow]data:[/b yellow]
      [magenta]first name:[/magenta] [b i blue]{main_character.first_name}[/b i blue]
      [magenta]last name:[/magenta] [b i blue]{main_character.last_name}[/b i blue]
      [magenta]gender:[/magenta] [b i blue]{main_character.gender}[/b i blue]
      [magenta]biography:[/magenta] [b i blue]{main_character.bio}[/b i blue]
    [b yellow]needs:[/b yellow]
      [magenta]bladder:[/magenta] [b i blue]{main_character.bladder}[/b i blue]
      [magenta]hunger:[/magenta] [b i blue]{main_character.hunger}[/b i blue]
      [magenta]energy:[/magenta] [b i blue]{main_character.energy}[/b i blue]
      [magenta]fun:[/magenta] [b i blue]{main_character.fun}[/b i blue]
      [magenta]social:[/magenta] [b i blue]{main_character.social}[/b i blue]
      [magenta]hygiene:[/magenta] [b i blue]{main_character.hygiene}[/b i blue]
    [b yellow]budget:[/b yellow]
      [magenta]money:[/magenta] [b i blue]${main_character.money}[/b i blue]
    [b yellow]interactions:[/b yellow]
      [b cyan]home:[/b cyan]
        [magenta]fridge[/magenta] - [white]see contents of the fridge[/white]
      [b cyan]money:[/b cyan]
        [magenta]work[/magenta] - [white]get to work[/white]
      [b cyan]buy:[/bold cyan]
        [magenta]grocery[/magenta] - [white]grocery store[/white]
      [b cyan]game:[/b cyan]
        [magenta]menu[/magenta] - [white]quit to main menu[/white]
        [magenta]exit[/magenta] - [white]quit simulat[/white]
    ''')

    choice = Prompt.ask('[bold green]panel',
                        choices=['fridge',
                                 'grocery',
                                 'work',
                                 'skip',
                                 'menu',
                                 'exit'],
                        default='skip',
                        show_choices=False)
    if choice == 'fridge':
        home_fridge.interact()

    elif choice == 'grocery':
        grocery_store()

    elif choice == 'work':
        work.menu()

    elif choice == 'skip':
        main_character.deplete_needs()
        panel()

    elif choice == 'menu':
        from main import start_game  # import game start to exit to start menu

        choice = Confirm.ask('are you sure?', default=False)
        if choice:
            start_game()
        else:
            panel()

    elif choice == 'exit':
        choice = Confirm.ask('are you sure?', default=False)
        if choice:
            exit()
        else:
            panel()
