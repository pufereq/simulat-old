#!/usr/bin/python3

# imports
from tracemalloc import start
from rich import print
from rich.prompt import IntPrompt
# game libs imports
from menus.menu import main_menu
"""
The Simulat Game
WIP
"""

def start_game():
    print("""
Welcome to...[bold green]
          _                    _         _   
         (_)                  | |       | |  
     ___  _  _ __ ___   _   _ | |  __ _ | |_ 
    / __|| || '_ ` _ \ | | | || | / _` || __|
    \__ \| || | | | | || |_| || || (_| || |_ 
    |___/|_||_| |_| |_| \__,_||_| \__,_| \__|[/bold green]
          [italic]by pufereq [[bold]Work in Progress[/bold]][/italic]
""")
    main_menu()

if __name__ == '__main__':
    start_game()