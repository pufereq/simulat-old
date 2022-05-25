#!/usr/bin/env python3

# game

# imports
from rich import print
from rich.prompt import Prompt
import os

from checks.os_check import clear
from txt.random_data import random_first, random_gender, random_last

class Character():
    def __init__(self, first_name, last_name, gender, bio):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.bio = bio

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
    os.system(clear())
    print('[bold red]DEBUG[/bold red]')
    print(f'{main_character.first_name=}\n{main_character.last_name=}\n{main_character.gender=}\n{main_character.bio=}\n\n')

    # print(f'[bold green]simulat[/bold green]\n[italic yellow]panel[/italic yellow]')
    print(f'''
[bold green]simulat[/bold green]
  [red]panel:[/red]
    [bold yellow]data:[/bold yellow]
      [magenta]first name:[/magenta] [italic blue]{main_character.first_name}[/italic blue]
      [magenta]last name:[/magenta] [italic blue]{main_character.last_name}[/italic blue]
      [magenta]gender:[/magenta] [italic blue]{main_character.gender}[/italic blue]
      [magenta]biography:[/magenta] [italic blue]{main_character.bio}[/italic blue]
    [bold yellow]stats:[/bold yellow]
      [magenta]bladder:[/magenta] [italic blue]not implemented[/italic blue]
      [magenta]hunger:[/magenta] [italic blue]not implemented[/italic blue]
      [magenta]energy:[/magenta] [italic blue]not implemented[/italic blue]
      [magenta]fun:[/magenta] [italic blue]not implemented[/italic blue]
      [magenta]social:[/magenta] [italic blue]not implemented[/italic blue]
      [magenta]hygiene:[/magenta] [italic blue]not implemented[/italic blue]
    [bold yellow]interactions:[/bold yellow]
      [magenta]NOT IMPLEMENTED[/magenta]
    ''')