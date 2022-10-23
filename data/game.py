#!/usr/bin/env python3
"""Main game.

Returns:
    None
"""
# game

# imports
from rich.prompt import Prompt, IntPrompt, Confirm

from data.classes.Character.character import Character
from data.classes.Fridge.fridge import Fridge
from data.classes.Work.work import Work
from data.classes.rooms.Bathroom.bathroom import Bathroom

from data.clear import clear
from data.res.get_names import random_first, random_gender, random_last
from data.res.random_data import random_fridge
from data.utils import error_handler, print_header, print_state


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
        from main import start_game
        first_name = None
        last_name = None
        gender = None
        bio = None
        while True:
            prompt = print_header("new game", [], "create a simulat",
                                  [{'category_name': "simulat data", 'data':
                                    [{'name': "first name", 'desc': first_name, 'interaction': False},
                                     {'name': "last name", 'desc': last_name, 'interaction': False},
                                     {'name': "gender", 'desc': gender, 'interaction': False},
                                     {'name': "biography", 'desc': bio, 'interaction': False}]}],
                                  'interactions:',
                                  [{'category_name': "change data", 'data':
                                    [{'name': "first", 'desc': "change first name", 'interaction': True},
                                     {'name': "last", 'desc': "change last name", 'interaction': True},
                                     {'name': "gender", 'desc': "change gender", 'interaction': True},
                                     {'name': "bio", 'desc': "change biography", 'interaction': True}]},
                                   {'category_name': "game", 'data':
                                    [{'name': "done", 'desc': "start the game", 'interaction': True}]}],
                                  clear_screen=True, go_back=start_game)
            if prompt == 'first':
                print("TIP: you can randomize data by inputing 'random' below.")
                first_name = Prompt.ask("first name")
                if first_name == 'random':
                    first_name = random_first()
            elif prompt == 'last':
                print("TIP: you can randomize data by inputing 'random' below.")
                last_name = Prompt.ask("last name")
                if last_name == 'random':
                    last_name = random_last()
            elif prompt == 'gender':
                print("TIP: you can randomize data by inputing 'random' below.")
                gender = Prompt.ask("gender")
                if gender == 'random':
                    gender = random_gender()
            elif prompt == 'bio':
                bio = Prompt.ask("bio")
            elif prompt == 'done':
                if first_name and last_name and gender is not None:
                    break
                else:
                    print_state("create a simulat",
                                "you have to fill these fields: first name; last name; gender.",
                                redirect=None, level=2, confirm=False)

        main_character = Character(first_name, last_name, gender, bio)
        home_fridge = Fridge(random_fridge(), random_fridge(), random_fridge(),
                             random_fridge(), random_fridge(), random_fridge())
    bathroom = Bathroom()
    work = Work()
    panel()


def grocery_store():
    """Buy foodstuffs."""
    fridge_contents = home_fridge.fridge_contents()
    prompt = print_header("buy", [], "grocery store",
                          [{'category_name': "fridge contents", 'data':
                            [{'name': "bread", 'desc': fridge_contents['bread'], 'interaction': False},
                             {'name': "vegetables", 'desc': fridge_contents['vegetables'], 'interaction': False},
                             {'name': "fruits", 'desc': fridge_contents['fruits'], 'interaction': False},
                             {'name': "eggs", 'desc': fridge_contents['eggs'], 'interaction': False},
                             {'name': "flour", 'desc': fridge_contents['flour'], 'interaction': False},
                             {'name': "meat", 'desc': fridge_contents['meat'], 'interaction': False}]},
                           {'category_name': "buy", 'data':
                            [{'name': "bread", 'desc': "$3", 'interaction': False},
                             {'name': "vegetables", 'desc': "$2", 'interaction': False},
                             {'name': "fruits", 'desc': "$2", 'interaction': False},
                             {'name': "eggs", 'desc': "$4", 'interaction': False},
                             {'name': "flour", 'desc': "$1", 'interaction': False},
                             {'name': "meat", 'desc': "$6", 'interaction': False}]}],
                          'interactions:',
                          [{'category_name': "buy", 'data':
                           [{'name': "bread", 'desc': "buy bread", 'interaction': True},
                            {'name': "vegetables", 'desc': "buy vegetables", 'interaction': True},
                            {'name': "fruits", 'desc': "buy fruits", 'interaction': True},
                            {'name': "eggs", 'desc': "buy eggs", 'interaction': True},
                            {'name': "flour", 'desc': "buy flour", 'interaction': True},
                            {'name': "meat", 'desc': "buy meat", 'interaction': True}]}],
                          go_back=panel, clear_screen=True)

    quantity = IntPrompt.ask('quantity')
    if prompt == 'bread':
        home_fridge.add_to_fridge('bread', quantity)

    elif prompt == 'vegetables':
        home_fridge.add_to_fridge('vegetables', quantity)

    elif prompt == 'fruits':
        home_fridge.add_to_fridge('fruits', quantity)

    elif prompt == 'eggs':
        home_fridge.add_to_fridge('eggs', quantity)

    elif prompt == 'flour':
        home_fridge.add_to_fridge('flour', quantity)

    elif prompt == 'meat':
        home_fridge.add_to_fridge('meat', quantity)
    grocery_store()


def panel():
    """Game panel.

    Shows data, allows to interact with game.
    """
    clear()
    prompt = print_header('game', [], 'panel',
                          [{'category_name': "simulat data", 'data':
                            [{'name': "first name", 'desc': main_character.first_name, 'interaction': False},
                             {'name': "last name", 'desc': main_character.last_name, 'interaction': False},
                             {'name': "gender", 'desc': main_character.gender, 'interaction': False},
                             {'name': "bio", 'desc': main_character.bio, 'interaction': False}]},
                           {'category_name': "needs", 'data':
                            [{'name': "bladder", 'desc': main_character.bladder, 'interaction': False},
                             {'name': "hunger", 'desc': main_character.hunger, 'interaction': False},
                             {'name': "energy", 'desc': main_character.energy, 'interaction': False},
                             {'name': "fun", 'desc': main_character.fun, 'interaction': False},
                             {'name': 'social', 'desc': main_character.social, 'interaction': False},
                             {'name': 'hygiene', 'desc': main_character.hygiene, 'interaction': False}]},
                           {'category_name': "budget", 'data':
                            [{'name': "money", 'desc': f"${main_character.money}", 'interaction': False}]}],
                          'interactions:',
                          [{'category_name': "home", 'data':
                            [{'name': "fridge", 'desc': 'see contents of the fridge', 'interaction': True},
                             {'name': "bathroom", 'desc': "go to the bathroom", 'interaction': True}]},
                           {'category_name': "money", 'data':
                            [{'name': "work", 'desc': "go to work", 'interaction': True}]},
                           {'category_name': "buy", 'data':
                            [{'name': "grocery", 'desc': "go to the grocery store", 'interaction': True}]},
                           {'category_name': "game", 'data':
                            [{'name': "skip", 'desc': "skip a turn", 'interaction': True},
                             {'name': "menu", 'desc': "quit to main menu", 'interaction': True},
                             {'name': "exit", 'desc': "quit simulat", 'interaction': True}]}], default='skip')
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
