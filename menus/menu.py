#!/usr/bin/env python3

# simulat menus
import os
from rich import print
from rich.prompt import IntPrompt

from dialogs.game import new_game

def main_menu():
    # main menu
    print("""
1. New Game
2. Load Game
3. Exit
9. debug
""")
    choice = IntPrompt.ask('main menu', choices=['1', '2', '3', '9'])
    if choice == 1:
        new_game(False)
    elif choice == 2:
        raise NotImplementedError('Not Implemented')
    elif choice == 3:
        exit()
    elif choice == 9:
        new_game(True)