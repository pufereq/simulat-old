#!/usr/bin/env python3
"""Main game.

Returns:
    None
"""
# game

# imports
import time

from rich import print
from rich.prompt import Prompt, IntPrompt, Confirm

from data.classes.Character.character import Character
from data.classes.Fridge.fridge import Fridge
from data.classes.Work.work import Work
from data.classes.rooms.Bathroom.bathroom import Bathroom

from data.clear import clear
from data.random.get_names import random_first, random_gender, random_last
from data.random.random_data import random_fridge
from data.utils import print_header


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
    global bathroom
    if debug:
        main_character = Character('DEBUG', 'DEBUG', 'DEBUG', 'DEBUG')
        home_fridge = Fridge(10, 10, 10, 10, 10, 10)
    else:
        clear()
        print("[bold green]Create a new simulat[/bold green]")
        first_name = Prompt.ask("[magenta]First name[/magenta]",
                                default=random_first())
        last_name = Prompt.ask("[magenta]Last name[/magenta]",
                               default=random_last())
        gender = Prompt.ask("[magenta]Gender[/magenta]",
                            default=random_gender())
        bio = Prompt.ask("[magenta]Biography[/magenta]",
                         default='None')
        if bio == 'None':
            bio = None

        main_character = Character(first_name, last_name, gender, bio)
        home_fridge = Fridge(random_fridge(), random_fridge(), random_fridge(),
                             random_fridge(), random_fridge(), random_fridge())
    bathroom = Bathroom()
    work = Work()
    panel()


def grocery_store():
    """Buy foodstuffs."""
    clear()
    print(f"""[b green]simulat[/b green]
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

        [magenta]back[/magenta] - [white]back to panel[/white]""")
    choice = Prompt.ask('grocery store',
                        choices=['bread', 'vegetables', 'fruits',
                                 'eggs', 'flour', 'meat', 'back'],
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
#     print(f"""[b green]simulat[/b green]
#   [red]panel:[/red]
#     [b yellow]data:[/b yellow]
#       [magenta]first name:[/magenta] [b i blue]{main_character.first_name}[/b i blue]
#       [magenta]last name:[/magenta] [b i blue]{main_character.last_name}[/b i blue]
#       [magenta]gender:[/magenta] [b i blue]{main_character.gender}[/b i blue]
#       [magenta]biography:[/magenta] [b i blue]{main_character.bio}[/b i blue]
#     [b yellow]needs:[/b yellow]
#       [magenta]bladder:[/magenta] [b i blue]{main_character.bladder}[/b i blue]
#       [magenta]hunger:[/magenta] [b i blue]{main_character.hunger}[/b i blue]
#       [magenta]energy:[/magenta] [b i blue]{main_character.energy}[/b i blue]
#       [magenta]fun:[/magenta] [b i blue]{main_character.fun}[/b i blue]
#       [magenta]social:[/magenta] [b i blue]{main_character.social}[/b i blue]
#       [magenta]hygiene:[/magenta] [b i blue]{main_character.hygiene}[/b i blue]
#     [b yellow]budget:[/b yellow]
#       [magenta]money:[/magenta] [b i blue]${main_character.money}[/b i blue]
#     [b yellow]interactions:[/b yellow]
#       [b cyan]home:[/b cyan]
#         [magenta]fridge[/magenta] - [white]see contents of the fridge[/white]
#         [magenta]bathroom[/magenta] - [white]go to the bathroom[/white]
#       [b cyan]money:[/b cyan]
#         [magenta]work[/magenta] - [white]get to work[/white]
#       [b cyan]buy:[/bold cyan]
#         [magenta]grocery[/magenta] - [white]grocery store[/white]
#       [b cyan]game:[/b cyan]
#         [magenta]menu[/magenta] - [white]quit to main menu[/white]
#         [magenta]exit[/magenta] - [white]quit simulat[/white]
#     """)
#
#     choice = Prompt.ask('[bold green]panel',
#                         choices=['fridge', 'grocery', 'work', 'bathroom',
#                                  'skip', 'menu', 'exit'],
#                         default='skip',
#                         show_choices=False)
    prompt = print_header('game', [], 'panel',
                          [{'category_name': "simulat data", 'data':
                            [{'name': "first name", 'desc': main_character.first_name},
                             {'name': "last name", 'desc': main_character.last_name},
                             {'name': "gender", 'desc': main_character.gender},
                             {'name': "bio", 'desc': main_character.bio}]},
                           {'category_name': "needs", 'data':
                            [{'name': "bladder", 'desc': main_character.bladder},
                             {'name': "hunger", 'desc': main_character.hunger},
                             {'name': "energy", 'desc': main_character.energy},
                             {'name': "fun", 'desc': main_character.fun},
                             {'name': 'social', 'desc': main_character.social},
                             {'name': 'hygiene', 'desc': main_character.hygiene}]},
                           {'category_name': "budget", 'data':
                            [{'name': "money", 'desc': f"${main_character.money}"}]}],

                          'interactions:', [],

                          [{'category_name': "home", 'data':
                            [{'name': "fridge", 'desc': 'see contents of the fridge'},
                             {'name': "bathroom", 'desc': "go to the bathroom"}]},
                           {'category_name': "money", 'data':
                            [{'name': "work", 'desc': "go to work"}]},
                           {'category_name': "buy", 'data':
                            [{'name': "grocery", 'desc': "go to the grocery store"}]},
                           {'category_name': "game", 'data':
                            [{'name': "skip", 'desc': "skip a turn"},
                             {'name': "menu", 'desc': "quit to main menu"},
                             {'name': "exit", 'desc': "quit simulat"}]}], default='skip')
    if prompt == 'fridge':
        home_fridge.interact()

    elif prompt == 'grocery':
        grocery_store()

    elif prompt == 'work':
        work.menu()

    elif prompt == 'bathroom':
        bathroom.room()

    elif prompt == 'skip':
        main_character.deplete_needs()
        panel()

    elif prompt == 'menu':
        from main import start_game  # import game start to exit to start menu

        prompt = Confirm.ask("are you sure?", default=False)
        if prompt:
            start_game()
        else:
            panel()

    elif prompt == 'exit':
        choice = Confirm.ask("are you sure?", default=False)
        if choice:
            exit()
        else:
            panel()
