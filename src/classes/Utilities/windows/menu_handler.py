#!/usr/bin/env python3
"""Curses menu handler."""

import curses as cs
from curses import panel


class Menu():
    """Menu generation using curses."""

    def __init__(self, title: str, items: list[dict], window: any, position: str = 'center', text_alignment: str = 'center') -> None:
        """Initialize Menu class.

        Args:
            title (str): Menu title.
            items (list[dict]): Menu items. See below for examples.
            window (Any): Window to display menu in.
            position (str): Position of the menu. Available values: 'center', 'bottom'. Defaults to 'center'.
            text_alignment (str): Alignment of text on menu buttons. Available values 'center', 'left'. Defaults to 'center'.

        Examples:
            items=[
                {
                    'label': "(str) Label of the button".
                    'target': "(func | None) Target function".
                    Leave none if checked manually using menu.result().
                    'args': "(dict) Function arguments. Leave empty if none."
                },
                {
                    'label': "foo",
                    'target': bar,
                    'args': {'name': "John Doe"}
                },
                ...
            ]
        """
        # init panels
        self.vertical_length = len(items)
        self.size = window.getmaxyx()
        self.text_alignment = text_alignment

        labels = list((_dict['label'] for _, _dict in enumerate(items)))
        labels.append(title)
        self.horizontal_length = int(len(max(labels, key=len)) + 4)
        labels.remove(title)
        try:
            self.window_border = window.subwin(
                self.vertical_length + 2,
                self.horizontal_length + 4,
                (self.size[0] // 2) - self.horizontal_length if position == 'center' else self.size[0] - self.vertical_length - 2,
                (self.size[1]) // 2 - self.vertical_length - 4
            )
            self.window = window.subwin(
                self.vertical_length + 2,
                self.horizontal_length + 4,
                (self.size[0] // 2) - self.horizontal_length if position == 'center' else self.size[0] - self.vertical_length - 2,
                (self.size[1]) // 2 - self.vertical_length - 4
            )
            # self.window_border = window.subwin(self.vertical_length + 2, self.horizontal_length + 2, (self.size[0] // 2 - self.horizontal_length) - 5 if not compact else - 0, ((self.size[1] - self.vertical_length - 4) // 2) - 5 if not compact else - 0)
            # self.window = window.subwin(self.vertical_length + 2, self.horizontal_length + 2, (self.size[0] // 2 - self.horizontal_length) - 5 if not compact else - 0, ((self.size[1] - self.vertical_length - 4) // 2) - 5 if not compact else - 0)
        except cs.error:
            raise Exception("Window too small!")
        # self.window = stdscr.subwin(0, 0)
        self.window_border.border()
        self.window_border.addstr(0, 1, title)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        # self.panel.border()
        self.panel.hide()
        panel.update_panels()

        self.pos = 0
        self.items = items
        # self.items.append(
        #     {
        #         'name': 'exit',
        #         'label': "exit",
        #         'target': exit,
        #         'args': {}
        #     }
        # )

    def navigate(self, n):
        self.pos += n
        if self.pos < 0:
            self.pos = 0
        elif self.pos >= len(self.items):
            self.pos = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()
        # self.window.clear()

        while True:
            self.window.refresh()
            cs.doupdate()
            for idx, item in enumerate(self.items):
                label = item['label']
                label_highlighted = '> ' + item['label'] + ' <'

                if idx == self.pos:
                    mode = cs.A_REVERSE
                    label = label_highlighted
                else:
                    label = '  ' + label + '  '
                    mode = cs.A_NORMAL

                label_len = len(label)
                left_spacing = 1
                if label_len % 2 == 0:
                    right_spacing = 0
                else:
                    right_spacing = 1
                if self.text_alignment == 'center':
                    label = ' ' * ((self.window.getmaxyx()[1] - label_len) // 2 - left_spacing) + label + ' ' * ((self.window.getmaxyx()[1] - label_len) // 2 - right_spacing)
                self.window.addstr(1 + idx, 1, label, mode)

            key = self.window.getch()

            if key in [cs.KEY_ENTER, ord('\n')]:
                global result
                target = self.items[self.pos]
                result = target['name']

                if target['target'] is None:
                    break

                if type(target['args']) is dict:
                    target['target'](**target['args'])
                elif type(target['args']) is list:
                    target['target'](*target['args'])

            elif key in (cs.KEY_UP, ord('k')):
                self.navigate(-1)
            elif key in (cs.KEY_DOWN, ord('j')):
                self.navigate(1)

        # cleanup
        # self.window.clear()
        self.panel.hide()
        panel.update_panels()
        cs.doupdate()

    def results(self) -> str:
        return result
