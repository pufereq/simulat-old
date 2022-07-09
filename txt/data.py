#!/usr/bin/env python3

"""Get data from files.

Returns:
    None
"""

import random as rn


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


def random_last():
    """Return random surname.

    From last.txt

    Returns:
        str: Random choice from surnames list.
    """
    with open('txt/last.txt') as last:
        return rn.choice((last.read().splitlines()))


def random_first_male():
    """Return random male first name.

    From first_male.txt

    Returns:
        str: Random choice from first male names list.
    """
    with open('txt/first_male.txt') as male:
        return rn.choice((male.read().splitlines()))


def random_first_female():
    """Return random female first name.

    From first_female.txt

    Returns:
        str: Random choice from first female names list.
    """
    with open('txt/first_female.txt') as female:
        return rn.choice((female.read().splitlines()))


def random_first():
    """Return random male or female first name.

    From first_male.txt and first_female.txt

    Returns:
        str: Random choice from male and female first names list.
    """
    with open('txt/first_male.txt') as male:
        male = male.read().splitlines()
    with open('txt/first_female.txt') as female:
        female = female.read().splitlines()
    return rn.choice(male + female)


def random_gender():
    """Return random gender.

    From genders.txt

    Returns:
        _type_: _description_
    """
    with open('txt/genders.txt') as genders:
        return rn.choice(genders.read().splitlines())


def random_deplete():
    """Return a random number from 0 to 3.

    Used in deplete_needs()

    Returns:
        int: Random number from 0 to 3.
    """
    return rn.randint(0, 3)


def random_money():
    """Return a random number from 50 to 500.

    Used in new_game()

    Returns:
        int: Random number from 50 to 500.
    """
    return rn.randint(50, 500)


def random_fridge():
    """Return a random number from 0 to 10.

    Used in new_game() when initializing Fridge()

    Returns:
        int: Random number from 0 to 10.
    """
    return rn.randint(0, 10)


def random_rob():
    """Return a dict containing details for rob().

    Returns:
        dict: Contains:
            money: Random number from 0 to 1000.
            got_caught: Random bool.
            rob_time: Random number from 3 to 14 (seconds).
    """
    return {'money': rn.randint(0, 1000), 'got_caught': rn.choice([True, False]), 'rob_time': rn.randint(3, 14)}
