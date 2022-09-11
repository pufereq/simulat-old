#!/usr/bin/env python3
"""Utilities."""

import time

from rich import print
from rich.prompt import Prompt

from data.clear import clear


def cap(value: int, min_value: int = 0, max_value: int = 100, throw_error=False) -> int:
    """Caps a number between miv_value and max_value.

    Args:
        value (int): Number to cap.
        min_value (int, optional): Low value to cap to. Defaults to 0.
        max_value (int, optional): High value to cap to. Defaults to 100.
        throw_error (bool, optional): _description_. Defaults to False.

    Returns:
        int: Capped value
    """
    if value < min_value:
        if throw_error:
            print(f"[red]value too small ({value} < {min_value})")
        value = min_value
    elif value > max_value:
        if throw_error:
            print(f"[red]value too large ({value} > {max_value})")
        value = max_value
    return value


def change_value(value: int, change: int, set: bool = False,
                 min_value: int = 0, max_value: int = 100,
                 cap_value: bool = True, return_old_and_new: bool = True) -> any:
    """Change value by change and caps by default.

    Args:
        value (int): Value to change
        change (int): Amount to change
        min_value (int, optional): Low value to cap to. Defaults to 0.
        max_value (int, optional): High value to cap to. Defaults to 100.
        cap_value (bool, optional): Should cap value. Defaults to True.

    Returns:
        int: changed (and capped) value.
        dict: old value and new (capped) value.
    """
    old_value = value
    if not set:
        value += change
        value = cap(value, min_value, max_value)
    else:
        value = change

    if return_old_and_new:
        return {'old': old_value, 'new': value}
    else:
        return value


def print_header(second_level_name: str, third_level_name: str,
                 fourth_level_name: str, interaction_list: list,
                 clear_screen=False, use_prompt=True, go_back=None) -> str:
    """Print header for menus.

    Adds back to interaction_list to go back.

    Args:
        second_level_name (str): second level name, see below
        third_level_name (str): third level name, see below
        fourth_level_name (str): fourth level ane, see below
        interaction_list (list): list of available interactions
        clear_screen (bool, optional): should clear screen. Defaults to False.
        use_prompt (bool, optional): should use rich's prompt. Defaults to True.
        go_back (func, optional): should add an option for going back. Defaults to None.

    Example:
        simulat
          second_level_name:
            third_level_name:
              fourth_level_name:
                interactions:
                  interaction_list
        e.g.
        simulat
          rooms:
            garage:
              car:
                interactions:
                  wash - wash car
                  back - go back

    Returns:
        str: _description_
    """
    interaction_list.append({'name': 'back', 'desc': "Go back"})
    if use_prompt:
        names = []
    if clear_screen:
        clear()
    print(f"""[b green]simulat[/b green]
  [b red]{second_level_name}:[/b red]
    [b yellow]{third_level_name}:[/b yellow]
      [b cyan]{fourth_level_name}:[/b cyan]
        [b blue]interactions:[/b blue]""")

    for dict in interaction_list:
        print(f"          [magenta]{dict['name']}[/magenta] - {dict['desc']}")
        names.append(dict['name'])
    if use_prompt:
        prompt = Prompt.ask(f"{third_level_name}", choices=names, default='back', show_choices=False)
        if go_back is not None:
            if prompt == 'back':
                go_back()
        return prompt
        # print(prompt)
    # example: print_header('garden', 'interactions', [{'name': 'foo', 'desc': 'bar'}, {'name': 'test', 'desc': 'test'}])


def print_state(source: str, message: str,
                goto: str, sleep_time: float = 1.5,
                old_state: any = None, new_state: any = None,
                prefix: str = None, suffix: str = None,
                source_color: str = 'b yellow', message_color: str = 'yellow',
                clear_screen: bool = True) -> None:
    """Print state of operation to the user.

    e.g. You have used the toilet.

    Args:
        source (str): source of the operation, e.g. toilet
        message (str): message
        goto (func): function to go to after time passed.
        sleep_time (float, optional): time to display message before going to another function. Defaults to 1.5.
        old_state (any, optional): State before operation. Defaults to None.
        new_state (any, optional): State after operation. Defaults to None.
        prefix (str, optional): Prefix of state. Defaults to None.
        suffix (str, optional): Suffix of state. Defaults to None.
        source_color (str, optional): color of source (rich syntax). Defaults to 'b yellow'.
        message_color (str, optional): color of message (rich syntax). Defaults to 'yellow'.
        clear_screen (bool, optional): should clear screen. Defaults to True.
    """
    if prefix is None:
        prefix = ''
    if suffix is None:
        suffix = ''
    if clear_screen:
        clear()
    print(f"[{source_color}]{source}: [/{source_color}][{message_color}]{message}")
    if old_state and new_state is not None:
        print(f"[{source_color}]State: [/{source_color}][red]{prefix}{old_state}{suffix}[/red] \
[{message_color}]>[/{message_color}] [green]{prefix}{new_state}{suffix}[/green]")
    time.sleep(sleep_time)
    goto()
