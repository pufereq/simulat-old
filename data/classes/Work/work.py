"""Work class."""

import time

from rich.progress import track
from rich.prompt import Prompt
from rich import print


from data.clear import clear
# from dialogs.game import panel, main_character
from data.txt.random_data import get_work_data, random_rob


class Work():
    """A work class, can add or take money."""

    def __init__(self):
        """Initializates work, currently does nothing."""
        # self.workplace = None
        pass

    def menu(self):
        """Work menu, can pick different jobs."""
        from data.game import panel
        clear()
        print(f'''[b green]simulat[/b green]
    [red]work:[/red]
        [b yellow]menu:[/b yellow]
        [magenta]newspaper[/magenta] - [white]deliver newspapers ($15 / takes 9 seconds)[/white]
        [magenta]pizza[/magenta] - [white]deliver pizzas ($20 / takes 10 seconds)[/white]
        [magenta]office[/magenta] - [white]work at an office ($40 / takes 19 seconds)[/white]
        [magenta]rob[/magenta] - [white]rob people (may earn up to $1000 (risky!))[/white]
        ''')
        choice = Prompt.ask('work',
                            choices=['newspaper', 'pizza', 'office',
                                     'rob', 'back'],
                            default='back',
                            show_choices=False)
        if choice == 'back':
            panel()
        elif choice == 'rob':
            self.rob()
        else:
            self.work(choice)

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
                           description=f'[i yellow]working... ({workplace})'):
                time.sleep(0.01)
        except KeyboardInterrupt:
            print('aborted')
        main_character.money += work_pay
        print(f'[i yellow]you now have {main_character.money}.')
        time.sleep(2)
        self.menu()

    def rob(self):
        """Use rich's track to 'visualize' robbing progess."""
        from data.game import main_character
        clear()
        rob_data = random_rob()
        try:
            for i in track(range(rob_data['rob_time'] * 100),
                           description=f'[i yellow]roaming the streets...'):
                time.sleep(0.01)
        except KeyboardInterrupt:
            print('aborted')

        if rob_data['got_caught']:
            if rob_data['money'] == 0:
                print('[i yellow]you have lost all of your stolen money while running away from the police')
                self.menu()

            print(f'[i yellow]police has caught you! you have to pay a [b red]${rob_data["money"]}[/b red] fine.')
            main_character.money -= rob_data['money']
        else:
            if rob_data['money'] == 0:
                print('[i yellow]you have bumped into a stranger and lost your money')
                self.menu()

            print(f'[i yellow]you have stolen [b red]${rob_data["money"]}')
            main_character.money += rob_data['money']
        print(f'[i yellow]you now have ${main_character.money}.')
        time.sleep(2)
        self.menu()
