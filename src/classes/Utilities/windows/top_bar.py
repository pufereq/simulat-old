#!/usr/bin/env python3

import curses as cs


class TopBar():
    """
    Top Bar class. Used to inform user of basic game state (debug text,
    title of current screen, details). Layout as follows:
    /----------------------------------------------------------------\
    |debug text                   title                      details |
    |----------------------------------------------------------------|
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
   ...                                                              ...

    debug text - used to display debug statuses. Defaults to 'simulat'
    on __init__.

    title - set to current screen (action) name e.g. panel.

    details - displays game time. (TODO)
    """
    def __init__(self, stdscr, debug_text: str = 'simulat'):
        from src.game.init import RED
        """Initialize top bar.

        Args:
            stdscr (_CursesWindow): Standard (main) screen.
            debug_text (str): Debug text. Defaults to 'simulat'.
        """

        stdscr_height, stdscr_width = stdscr.getmaxyx()

        # create top bar
        self.top_bar = cs.newwin(1, stdscr_width, 0, 0)
        self.top_bar_height, self.top_bar_width = self.top_bar.getmaxyx()

        # create debug subwindow
        self.debug_win = self.top_bar.subwin(0, 20, 0, 0)
        self.debug_win_height, self.debug_win_width = self.debug_win.getmaxyx()

        # create title subwindow
        self.title_win = self.top_bar.subwin(0, self.top_bar_width - 40, 0, 20)
        self.title_height, self.title_width = self.title_win.getmaxyx()

        # create details subwindow
        self.details_win = self.top_bar.subwin(0, 20, 0, self.top_bar_width - 20)
        self.details_height, self.details_width = self.details_win.getmaxyx()

        # stylize bar
        self.debug_win.bkgd(' ', cs.A_REVERSE)
        self.title_win.bkgd(' ', cs.A_REVERSE)
        self.details_win.bkgd(' ', cs.A_REVERSE)
        self.top_bar.bkgd(' ', cs.A_REVERSE)

        # add debug text
        self.update_debug_win(debug_text)

        # DEBUG: add details text
        # self.update_details('TEST1234#')

        # DEBUG: add title
        # self.update_title('TEST1234#')

        # top_bar.addstr(str(len(main_character.first_name)))
        # details = ("time: soon")
        # self.top_bar.addstr(0, stdscr_width - len(details) - 1, details)
        stdscr.refresh()
        self.debug_win.refresh()
        self.title_win.refresh()
        self.details_win.refresh()
        self.top_bar.refresh()

    def clear_debug_win(self):
        self.debug_win.clear()
        self.debug_win.refresh()

    def update_debug_win(self, new_debug_text: str):
        self.debug_win.clear()
        self.debug_win.addstr(new_debug_text)
        self.debug_win.refresh()

    def clear_title(self):
        self.title_win.clear()
        self.title_win.refresh()

    def update_title(self, new_title: str):
        self.title_win.clear()
        self.title_win.addstr(0, (self.title_width - len(new_title)) // 2, new_title)
        # self.title_win.addstr(new_title)
        self.title_win.refresh()

    def clear_details(self):
        self.details_win.clear()
        self.details_win.refresh()

    def update_details(self, new_details: str):
        self.details_win.addstr(0, self.details_width - len(new_details) - 1, new_details)
        self.details_win.refresh()
