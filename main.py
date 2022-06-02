#!/usr/bin/python3

# imports
import os
import time

# check if rich is installed and install if not
try:
    from rich import print
    from rich.prompt import IntPrompt
except ImportError:
    print('Rich is not installed.\nInstalling Rich')
    time.sleep(1)
    os.system('pip install rich')
    print('\n\nRich is now installed. Extiting...')
    exit()

# game libs imports
from menus.menu import main_menu
from checks.os_check import clear

"""
The Simulat Game
WIP
"""

def start_game():
    '''
    game logo
    '''
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