#!/usr/bin/env python3

"""Get data from files.

Returns:
    None
"""

import random as rn

from data.utils import error_handler


@error_handler
def random_last():
    """Return random surname.

    From last.txt

    Returns:
        str: Random choice from surnames list.
    """
    with open("data/res/names/last.txt") as last:
        return rn.choice((last.read().splitlines()))


@error_handler
def random_first_male():
    """Return random male first name.

    From first_male.txt

    Returns:
        str: Random choice from first male names list.
    """
    with open("data/res/names/first_male.txt") as male:
        return rn.choice((male.read().splitlines()))


@error_handler
def random_first_female():
    """Return random female first name.

    From first_female.txt

    Returns:
        str: Random choice from first female names list.
    """
    with open("data/res/names/first_female.txt") as female:
        return rn.choice((female.read().splitlines()))


@error_handler
def random_first():
    """Return random male or female first name.

    From first_male.txt and first_female.txt

    Returns:
        str: Random choice from male and female first names list.
    """
    with open("data/res/names/first_male.txt") as male:
        male = male.read().splitlines()
    with open("data/res/names/first_female.txt") as female:
        female = female.read().splitlines()
    return rn.choice(male + female)


@error_handler
def random_gender():
    """Return random gender.

    From genders.txt

    Returns:
        _type_: _description_
    """
    with open("data/res/names/genders.txt") as genders:
        return rn.choice(genders.read().splitlines())