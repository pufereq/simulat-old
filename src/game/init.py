#!/usr/bin/env python3

import curses as cs
# from src.classes.Utilities.windows.notification import Notification
from src.classes.Utilities.windows.top_bar import TopBar
# from src.classes.Utilities.hex_to_composite import hex_to_comp


def init_curses():
    global stdscr, stdscr_height, stdscr_width

    stdscr = cs.initscr()
    stdscr_height, stdscr_width = stdscr.getmaxyx()

    cs.noecho()
    cs.cbreak()
    cs.curs_set(0)
    cs.start_color()
    return stdscr


def init_color():
    global BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

    # change colors to Nord theme if possible # TODO: add themes
    if cs.can_change_color():
        cs.init_color(0, 0, 0, 0)

    # init color pairs
    # cs.init_pair(0, cs.COLOR_WHITE, cs.COLOR_BLACK)
    cs.init_pair(1, cs.COLOR_RED, cs.COLOR_BLACK)
    cs.init_pair(2, cs.COLOR_GREEN, cs.COLOR_BLACK)
    cs.init_pair(3, cs.COLOR_YELLOW, cs.COLOR_BLACK)
    cs.init_pair(4, cs.COLOR_BLUE, cs.COLOR_BLACK)
    cs.init_pair(5, cs.COLOR_MAGENTA, cs.COLOR_BLACK)
    cs.init_pair(6, cs.COLOR_CYAN, cs.COLOR_BLACK)
    cs.init_pair(7, cs.COLOR_WHITE, cs.COLOR_BLACK)

    # assign color pairs to variables
    # 0:black, 1:red, 2:green, 3:yellow, 4:blue, 5:magenta, 6:cyan, and 7:white
    # BLACK = cs.color_pair(0)
    RED = cs.color_pair(1)
    GREEN = cs.color_pair(2)
    YELLOW = cs.color_pair(3)
    BLUE = cs.color_pair(4)
    MAGENTA = cs.color_pair(5)
    CYAN = cs.color_pair(6)
    WHITE = cs.color_pair(7)


def init_game_win():
    global game_win, game_win_height, game_win_width

    game_win = cs.newwin(stdscr_height - 1, stdscr_width, 1, 0)
    game_win_height, game_win_width = game_win.getmaxyx()


def init_topbar(stdscr, debug_text: str = 'simulat'):
    """Initialize TopBar and assign it to a variable.

    Args:
        stdscr (_CursesWindow): Standard screen.
        debug_text (str): Text displayed on left side of TopBar. Defaults to 'simulat'.
    """
    global top_bar
    top_bar = TopBar(stdscr, debug_text)


def init_notification(game_window):
    global notification

    notification = Notification(game_window)


def init_content_win(game_window):
    """Initialize content window.

    Args:
        game_window (_CursesWindow): Game window.
    """
