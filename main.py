#!/usr/bin/python3

# imports
from rich.console import Console
from rich.prompt import Prompt
import platform # for determining the OS

# define console
console = Console()

"""
The Simulat Game
WIP
"""
def menu():
    # main menu
    console.print("""
Welcome to...[bold green]
          _                    _         _   
         (_)                  | |       | |  
     ___  _  _ __ ___   _   _ | |  __ _ | |_ 
    / __|| || '_ ` _ \ | | | || | / _` || __|
    \__ \| || | | | | || |_| || || (_| || |_ 
    |___/|_||_| |_| |_| \__,_||_| \__,_| \__|[/bold green]
          [italic]by pufereq [[bold]Work in Progress[/bold]][/italic]

1. New Game
2. Load Game [wip]
3. Exit
""")
    choice = Prompt.ask('Main Menu', choices=['1', '2', '3'])
    assert choice
    if choice == 1:
        raise Exception('Not miplememe') # create a new game
    elif choice == 2:
        pass # load a game
    elif choice == 3:
        pass # exit
if __name__ == '__main__':
    menu()