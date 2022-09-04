#!/usr/bin/env python3
"""Utilities."""

from rich import print


def cap(value, min_value, max_value, throw_error=False):
    """Caps a number between miv_value and max_value.

    Args:
        value (_type_): _description_
        min_value (_type_): _description_
        max_value (_type_): _description_
        throw_error (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    if value < min_value:
        if throw_error:
            print('[red]value too small')
        value = min_value
    elif value > max_value:
        if throw_error:
            print('[red]value too large')
        value = max_value
    return value


test = cap(test, 0, 10)
print(f'{test=}')
