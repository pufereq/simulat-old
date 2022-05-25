#!/usr/bin/env python3

# game

# imports
from rich import print
from rich.prompt import Prompt
import os
import random as rn

from checks.os_check import clear
from txt.random_data import random_first, random_gender, random_last, random_deplete, random_money

class Character():
    def __init__(self, first_name, last_name, gender, bio):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.bio = bio

        self.bladder = 100
        self.hunger = 100
        self.energy = 100
        self.fun = 100
        self.social = 100
        self.hygiene = 100
        self.money = random_money()
    def deplete_needs(self):
        self.bladder -= random_deplete()
        self.hunger -= random_deplete()
        self.energy -= random_deplete()
        self.fun -= random_deplete()
        self.social -= random_deplete()
        self.hygiene -= random_deplete()

def new_game(debug):
    global main_character

    if debug:
        main_character = Character('DEBUG', 'DEBUG', 'DEBUG', 'DEBUG')
        panel()
    else: 
        os.system(clear())
        print('[bold green]Create a new simulat[/bold green]')
        first_name = Prompt.ask('[magenta]First name[/magenta]', default = random_first())
        last_name = Prompt.ask('[magenta]Last name[/magenta]', default = random_last())
        gender = Prompt.ask('[magenta]Gender[/magenta]', default = random_gender())
        bio = Prompt.ask('[magenta]Biography[/magenta]', default = 'None')
        if bio == 'None': bio = None

        main_character = Character(first_name, last_name, gender, bio)
        panel()

def panel():
    clear()
    # print('[bold red]DEBUG[/bold red]')
    # print(f'{main_character.first_name=}\n{main_character.last_name=}\n{main_character.gender=}\n{main_character.bio=}\n\n')

    # print(f'[bold green]simulat[/bold green]\n[italic yellow]panel[/italic yellow]')
    print(f'''
[bold green]simulat[/bold green]
  [red]panel:[/red]
    [bold yellow]data:[/bold yellow]
      [magenta]first name:[/magenta] [bold italic blue]{main_character.first_name}[/bold italic blue]
      [magenta]last name:[/magenta] [bold italic blue]{main_character.last_name}[/bold italic blue]
      [magenta]gender:[/magenta] [bold italic blue]{main_character.gender}[/bold italic blue]
      [magenta]biography:[/magenta] [bold italic blue]{main_character.bio}[/bold italic blue]
    [bold yellow]needs:[/bold yellow]
      [magenta]bladder:[/magenta] [bold italic blue]{main_character.bladder}[/bold italic blue]
      [magenta]hunger:[/magenta] [bold italic blue]{main_character.hunger}[/bold italic blue]
      [magenta]energy:[/magenta] [bold italic blue]{main_character.energy}[/bold italic blue]
      [magenta]fun:[/magenta] [bold italic blue]{main_character.fun}[/bold italic blue]
      [magenta]social:[/magenta] [bold italic blue]{main_character.social}[/bold italic blue]
      [magenta]hygiene:[/magenta] [bold italic blue]{main_character.hygiene}[/bold italic blue]
    [bold yellow]budget:[/bold yellow]
      [magenta]money:[/magenta] [bold italic blue]${main_character.money}[/bold italic blue]
    [bold yellow]interactions:[/bold yellow]
      [purple]buy:[/purple]
        [magenta]grocery - grocery store[/magenta]
      [magenta]COMING SOON[/magenta]
    ''')
    input()
    main_character.deplete_needs()
    panel()

def grocery_store():
    raise NotImplementedError()
