#!/usr/bin/python3

# imports
from rich import print
from rich.prompt import IntPrompt
import os
# game libs imports
from menus.menu import main_menu
from checks.os_check import clear

"""
The Simulat Game
WIP
"""

def start_game():
    clear()
    print('''
Welcome to...[bold green]
          _                    _         _   
         (_)                  | |       | |  
     ___  _  _ __ ___   _   _ | |  __ _ | |_ 
    / __|| || '_ ` _ \ | | | || | / _` || __|
    \__ \| || | | | | || |_| || || (_| || |_ 
    |___/|_||_| |_| |_| \__,_||_| \__,_| \__|[/bold green]
          [italic]by pufereq [[bold]Work in Progress[/bold]][/italic]
''')
    main_menu()

if __name__ == '__main__':
    start_game()
else:
    raise ImportError('Main script cannot be used as a module.')