"""Work class."""

import time

from rich.progress import track
from rich.prompt import Prompt
from rich import print


from data.clear import clear
from data.res.random_data import get_work_data, random_rob
from data.utils import change_value, error_handler, print_header, print_state


class Work():
    """A work class, can add or take money."""

    def __init__(self):
        """Initializates work, currently does nothing."""
        # self.workplace = None
        pass

    @error_handler
    def menu(self):
        """Work menu, can pick different jobs."""
        from data.game import panel
        prompt = print_header("money", [], "work", [], "interactions:",
                              [{'category_name': "work", 'data':
                                [{'name': "newspaper", 'desc': "deliver newspapers ($15 / 9s)", 'interaction': True},
                                 {'name': "pizza", 'desc': "deliver pizzas ($20 / 10s)", 'interaction': True},
                                 {'name': "office", 'desc': "work at an office ($40 / 19s)", 'interaction': True}]},
                               {'category_name': "risky", 'data':
                                [{'name': "rob", 'desc': "pickpocket (may earn $1000 / 3-14s)", 'interaction': True}]}],
                              clear_screen=True, go_back=panel)
        if prompt == 'back':
            panel()
        elif prompt == 'rob':
            self.rob()
        else:
            self.work(prompt)

    @error_handler
    def work(self, workplace):
        """Use rich's track to 'visualize' work progress.

        Args:
            workplace (str): Used in defining work time and pay.
        """
        from data.game import main_character
        clear()
        work_data = get_work_data(workplace)
        work_time = work_data['time']
        work_pay = work_data['pay']
        try:
            for i in track(range(work_time * 100),
                           description=f"[i yellow]working... ({workplace})"):
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("aborted")
        changed = change_value(main_character.money, work_pay, cap_value=False)
        print_state("work", f"you have worked ({workplace}) and got paid ${work_pay}",
                    None, 1, False,
                    old_state=changed['old'], new_state=changed['new'], prefix='$')
        main_character.money = changed['new']
        self.menu()

    @error_handler
    def rob(self):
        """Use rich's track to 'visualize' robbing progess."""
        from data.game import main_character
        clear()
        rob_data = random_rob()
        try:
            for i in track(range(rob_data['rob_time'] * 100),
                           description=f"[i yellow]roaming the streets..."):
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("aborted")

        if rob_data['got_caught']:
            if rob_data['money'] == 0:
                changed = change_value(main_character.money, rob_data['money'], cap_value=False, set=True)
                print_state("work", f"you have lost all your money while fleeing from the police.",
                            None, 1, False,
                            old_state=changed['old'], new_state=changed['new'], prefix='$')
            else:
                changed = change_value(main_character.money, -rob_data['money'], cap_value=False)
                print_state("work", f"police has caught you! you paid a ${rob_data['money']} fine.",
                            None, 1, False,
                            old_state=changed['old'], new_state=changed['new'], prefix='$')
        else:
            if rob_data['money'] == 0:
                changed = change_value(main_character.money, rob_data['money'], cap_value=False)
                print_state("work", f"you have bumped into a stranger and lost your stolen money.",
                            None, 1, False,
                            old_state=changed['old'], new_state=changed['new'], prefix='$')
            else:
                changed = change_value(main_character.money, rob_data['money'], cap_value=False)
                print_state("work", f"you have succesfully pickpocketed someone!",
                            None, 1, False,
                            old_state=changed['old'], new_state=changed['new'], prefix='$')
        if rob_data['got_caught']:
            main_character.money = changed['new']
        else:
            main_character.money = changed
        self.menu()
