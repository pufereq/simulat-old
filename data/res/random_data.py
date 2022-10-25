#!/usr/bin/env python3

"""Random data."""

import random as rn

from data.utils import error_handler


@error_handler
def get_work_data(workplace):
    """Return job details based on workplace argument.

    Args:
        workplace (str): workplace chosen in work menu.

    Returns:
        dict: Return how long a job lasts and its pay.
    """
    if workplace == 'newspaper':
        return {'pay': 15, 'time': 9}
    elif workplace == 'pizza':
        return {'pay': 20, 'time': 10}
    elif workplace == 'office':
        return {'pay': 40, 'time': 19}
    else:
        return False


@error_handler
def random_deplete():
    """Return a random number from 0 to 3.

    Used in deplete_needs()

    Returns:
        int: Random number from 0 to 3.
    """
    return rn.randint(0, 3)


@error_handler
def random_money():
    """Return a random number from 50 to 500.

    Used in new_game()

    Returns:
        int: Random number from 50 to 500.
    """
    return rn.randint(50, 500)


@error_handler
def random_fridge():
    """Return a random number from 0 to 10.

    Used in new_game() when initializing Fridge()

    Returns:
        int: Random number from 0 to 10.
    """
    return rn.randint(0, 10)


@error_handler
def random_rob():
    """Return a dict containing details for rob().

    Returns:
        dict: Contains:
            money: Random number from 0 to 1000.
            got_caught: Random bool.
            rob_time: Random number from 3 to 14 (seconds).
    """
    return {'money': rn.randint(0, 1000), 'got_caught': rn.choice([True, False]), 'rob_time': rn.randint(3, 14)}
