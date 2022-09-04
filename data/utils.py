#!/usr/bin/env python3
"""Utilities."""

from rich import print


def cap(value: int, min_value: int, max_value: int, throw_error=False) -> int:
    """Caps a number between miv_value and max_value.

    Args:
        value (int): Number to cap.
        min_value (int): Low value to cap to.
        max_value (int): High value to cap to.
        throw_error (bool, optional): _description_. Defaults to False.

    Returns:
        int: Capped value
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
