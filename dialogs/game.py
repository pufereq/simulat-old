#!/usr/bin/env python3

# game

# imports
from rich import print
from rich.prompt import Prompt, Confirm
import os
import random as rn

from checks.os_check import clear
from txt.random_data import random_first, random_fridge, random_gender, random_last, random_deplete, random_money

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

        self.check_needs()
    def check_needs(self):
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
    def __init__(self, bread, vegetables, fruits, eggs, flour, meat):
        self.bread = bread
        self.vegetables = vegetables
        self.fruits = fruits
        self.eggs = eggs
        self.flour = flour
        self.meat = meat


def new_game(debug):
    global main_character
    global fridge
    if debug:
        main_character = Character('DEBUG', 'DEBUG', 'DEBUG', 'DEBUG')
        fridge = Fridge(10, 10, 10, 10, 10, 10)
        panel()
    else: 
        clear()
        print('[bold green]Create a new simulat[/bold green]')
        first_name = Prompt.ask('[magenta]First name[/magenta]', default = random_first())
        last_name = Prompt.ask('[magenta]Last name[/magenta]', default = random_last())
        gender = Prompt.ask('[magenta]Gender[/magenta]', default = random_gender())
        bio = Prompt.ask('[magenta]Biography[/magenta]', default = 'None')
        if bio == 'None': bio = None

        main_character = Character(first_name, last_name, gender, bio)
        fridge = Fridge(random_fridge(), random_fridge(), random_fridge(), random_fridge(), random_fridge(), random_fridge())
        panel()

def fridge_contents():
    return(f'''  [bold yellow]fridge contents:
    [magenta]bread:[/magenta] [bold italic blue]{fridge.bread}[/bold italic blue]
    [magenta]vegetables:[/magenta] [bold italic blue]{fridge.vegetables}[/bold italic blue]
    [magenta]fruits:[/magenta] [bold italic blue]{fridge.fruits}[/bold italic blue]
    [magenta]eggs:[/magenta] [bold italic blue]{fridge.eggs}[/bold italic blue]
    [magenta]flour:[/magenta] [bold italic blue]{fridge.flour}[/bold italic blue]
    [magenta]meat:[/magenta] [bold italic blue]{fridge.meat}[/bold italic blue]''')


def grocery_store():
    print(f'''
[bold green]simulat[/bold green]
  [red]grocery store[/red]
    {fridge_contents()}
    ''')

def see_fridge():
    clear()
    print(f'''
[bold green]simulat[/bold green]
{fridge_contents()}
  [bold yellow]interactions:[/bold yellow]
    [magenta]eat - eat contents[/magenta]
    [magenta]back - go back to panel[/magenta]
''')
    choice = Prompt.ask('Fridge:', choices = ['eat', 'back'], default = 'back', show_choices = False)
    if choice == 'eat':
        print(f'''
  [bold yellow]eat raw[/bold yellow]
    [magenta]bread:[/magenta] [bold italic blue]+8 hunger; -1 fun[/bold italic blue]
    [magenta]vegetables:[/magenta] [bold italic blue]+5 hunger; +2 fun[/bold italic blue]
    [magenta]fruits:[/magenta] [bold italic blue]+7 hunger; +4 fun[/bold italic blue]
    [magenta]eggs:[/magenta] [bold italic blue]+3 hunger; -2 fun[/bold italic blue]
    [magenta]flour:[/magenta] [bold italic blue]+1 hunger; -10 fun; -5 hygiene[/bold italic blue]
    [magenta]meat:[/magenta] [bold italic blue]+6 hunger; -4 fun[/bold italic blue]
        ''')
        choice = Prompt.ask('eat raw', choices = ['bread', 'vegetables', 'fruits', 'eggs', 'flour', 'meat', 'back'], show_choices = False, default = 'back')
        if choice == 'bread':
            pass
        
    elif choice == 'back':
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
      [bold cyan]home:[/bold cyan]
        [magenta]fridge - see contents of the fridge[/magenta]
      [bold cyan]buy:[/bold cyan]
        [magenta]grocery - grocery store[/magenta]
      [bold cyan]game:[/bold cyan]
        [magenta]exit - quit simulat[/magenta]
    ''')
    choice = Prompt.ask('[bold green]panel', choices = ['fridge', 'grocery', 'skip', 'exit'], default = 'skip', show_choices = False)
    if choice == 'fridge':
        # raise NotImplementedError()
        see_fridge()
    elif choice == 'grocery':
        grocery_store()
    elif choice == 'skip':
        main_character.deplete_needs()
        panel()
    elif choice == 'exit':
        choice = Confirm.ask('Are you sure?', default = False)
        if choice: exit()
        else: panel()
