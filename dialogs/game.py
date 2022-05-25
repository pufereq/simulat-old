#!/usr/bin/env python3

# game

# imports
from rich import print
from rich.prompt import Prompt
import os

from checks.os_check import clear
from txt.random_data import random_first, random_gender, random_last

class Character():
    def __init__(self, first, last, gender, bio):
        self.first = first
        self.last = last
        self.gender = gender
        self.bio = bio

def new_game():
    global main_character
    os.system(clear())
    print('[bold green]Create a new simulat[/bold green]')
    first = Prompt.ask('[magenta]First name[/magenta]', default = random_first())
    last = Prompt.ask('[magenta]Last name[/magenta]', default = random_last())
    gender = Prompt.ask('[magenta]Gender[/magenta]', default = random_gender())
    bio = Prompt.ask('[magenta]Biography[/magenta]', default = 'None')
    if bio == 'None': bio = None

    main_character = Character(first, last, gender, bio)
    panel()

def panel():
    os.system(clear())
    # raise NotImplementedError()
    print('[bold red]DEBUG[/bold red]')
    print('[bold green]simulat alpha panel[/bold green]')
    print(f'{main_character.first=}\n{main_character.last=}\n{main_character.gender=}\n{main_character.bio=}\n')