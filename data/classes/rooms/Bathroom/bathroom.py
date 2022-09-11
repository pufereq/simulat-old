#!/usr/bin/env python3

from rich import print

from data.utils import change_value, print_header, print_state
from data.clear import clear

# bladder = 70  # temporary
# hygiene = 60  # temporary


class Bathroom():
    def __init__(self) -> None:
        pass

    def room(self):
        from data.game import panel
        clear()
        prompt = print_header("rooms", "bathroom", "room",
                              [{'name': 'toilet', 'desc': "use the toilet"},
                               {'name': 'sink', 'desc': "use the sink"},
                               {'name': 'shower', 'desc': "take a shower"}],
                              go_back=panel)
        if prompt == 'toilet':
            self.toilet()
        elif prompt == 'sink':
            self.sink()
        elif prompt == 'shower':
            self.shower()

    def toilet(self):
        from data.game import main_character
        # global bladder  # temporary
        clear()
        prompt = print_header("rooms", "bathroom", "toilet",
                              [{'name': 'use', 'desc': "use the toilet"},
                               {'name': 'quick', 'desc': "take a quick pee"}],
                              go_back=self.room)
        if prompt == 'use':
            changed = change_value(main_character.bladder, 100, set=True)
            main_character.bladder = changed['new']
            print_state('toilet', "You have used the toilet.",
                        self.toilet, old_state=changed['old'],
                        new_state=changed['new'], suffix='%')
        elif prompt == 'quick':
            changed = change_value(main_character.bladder, 50)
            main_character.bladder = changed['new']
            print_state('toilet', "You have used the toilet quickly.",
                        self.toilet, old_state=changed['old'],
                        new_state=changed['new'], suffix='%')

    def sink(self):
        from data.game import main_character
        # global hygiene  # temporary
        clear()
        prompt = print_header("rooms", "bathroom", "sink",
                              [{'name': 'use', 'desc': "wash hands"},
                               {'name': 'brush', 'desc': "brush teeth."}],
                              go_back=self.room)
        if prompt == 'use':
            changed = change_value(main_character.hygiene, 10)
            main_character.hygiene = changed['new']
            print_state('toilet', "You have used the sink.",
                        self.sink, old_state=changed['old'],
                        new_state=changed['new'], suffix='%')
        elif prompt == 'brush':
            changed = change_value(main_character.hygiene, 15)
            main_character.hygiene = changed['new']
            print_state('toilet', "You have brushed your teeth.",
                        self.sink, old_state=changed['old'],
                        new_state=changed['new'], suffix='%')

    def shower(self):
        from data.game import main_character
        # global hygiene  # temporary
        clear()
        prompt = print_header("rooms", "bathroom", "shower",
                              [{'name': 'use', 'desc': "take a shower"},
                               {'name': 'quick', 'desc': "take a quick shower"}],
                              go_back=self.room)
        if prompt == 'use':
            changed = change_value(main_character.hygiene, 100, set=True)
            main_character.hygiene = changed['new']
            print_state('toilet', "You have taken a shower.",
                        self.shower, old_state=changed['old'],
                        new_state=changed['new'], suffix='%')
        elif prompt == 'quick':
            changed = change_value(main_character.hygiene, 50)
            main_character.hygiene = changed['new']
            print_state('toilet', "You have taken a quick shower",
                        self.shower, old_state=changed['old'],
                        new_state=changed['new'], suffix='%')

