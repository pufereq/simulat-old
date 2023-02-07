#!/usr/bin/python3

"""simulat start."""

# imports
import curses as cs

from src.game.init import init_curses, init_game_win, init_topbar, init_color

# game libs imports
from src.menu import main_menu
from src.clear import clear


def init():
    stdscr = init_curses()
    init_color()
    init_game_win()
    from src.game.init import game_win
    init_topbar(stdscr)
    # init_notification(game_win)

    cs.wrapper(start_game, game_win)


def exit_game(code=0):
    cs.echo()
    cs.nocbreak()
    cs.endwin()
    exit(code)


def start_game(stdscr, game_window):
    from src.game.init import top_bar
    """Start simulat.

    Display logo, redirect to menu.
    """
    # stdscr.clear()
    height, width = stdscr.getmaxyx()
    top_bar.top_bar.refresh()
    text = "Welcome to simulat!"
    game_window.addstr(1, width // 2 - len(text) // 2, text)
    game_window.refresh()
    # game_window.getch()
    main_menu(game_window)


if __name__ == "__main__":
    init()
