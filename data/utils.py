#!/usr/bin/env python3
"""Utilities."""

import time

from rich import print
from rich.prompt import Prompt, Confirm

from data.clear import clear


def empty_var(var_type):
    """Return empty variable of specified type.

    Args:
        var_type (type): name of variable type. Available types:
        int; float; str; tuple; list; dict

    Returns:
        any: empty variable of specified type.
    """
    empty_vars = {int: int(), float: float(), str: str(),
                  tuple: tuple(), list: list(), dict: dict()}
    return empty_vars[var_type]


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
        if cap_value:
            value = cap(value, min_value, max_value)
    else:
        value = change

    if return_old_and_new:
        return {'old': old_value, 'new': value}
    else:
        return value


def print_header(second_level_name: str, second_level_contents: list,
                 third_level_name: str, third_level_contents: list,
                 interaction_cat_name: str, interaction_list: list,
                 clear_screen=False, use_prompt=True,
                 go_back=None, default=None) -> str | None:
    """Print header for menus.

    Adds back to interaction_list to go back.

    Args:
        second_level_name (str): second level name, see below
        second_level_contents (list): second level contents, see below
        third_level_name (str): third level name, see below
        third_level_contents (list): third level contents, see below
        interaction_cat_name (str): interaction category name, see below
        interaction_list (list): list of available interactions; if None, won't display interaction_cat_name
        clear_screen (bool, optional): should clear screen. Defaults to False.
        use_prompt (bool, optional): should use rich's prompt. Defaults to True.
        go_back (func, optional): should add an option for going back. Defaults to None.
        default (str, optional): should add default option in rich's prompt.
        If set to None, go_back takes over, if go_back = None, rich's default
        is set to None (doesn't display). Defaults to None.

    Example:
        simulat
          second_level_name:
            third_level_name:
              interaction_cat_name:
                interaction_list
        e.g.
        simulat
          rooms:
            garage:
              car:
                wash - wash car
                back - go back;
        simulat
          panel:
            Energy: 24%
            bedroom:
              bed:
                sleep - go to sleep
                back - go back

    interaction_list example syntax:
        interaction_list = [{'name': 'cat1', 'data':
                        [{'name': "foo", 'desc': "foodesc"},
                         {'name': "bar", 'desc': "bardesc"},
                         {'name': "zar", 'desc': "zardesc"}]},
                        {'name': 'cat2', 'data':
                         [{'name': "baz", 'desc': "bazdesc"}]},
                        {'name': None, 'data':
                         [{'name': "qaz", 'desc': "qazdesc"},
                          {'name': "waq", 'desc': "waqdesc"}]}]

    Returns:
        str: prompt input
        None: if use_prompt=False
    """
    global names
    names = []
    if go_back is None:
        include_back = False
    else:
        include_back = True
    if clear_screen:
        clear()
    print(f"""[b green]simulat[/b green]
  [b red]{second_level_name}:[/b red]""")
    print_category(second_level_contents, 6, False, 'red')
    print(f"    [b yellow]{third_level_name}:[/b yellow]")
    print_category(third_level_contents, 8, False, 'yellow')
    if use_prompt:
        print(f"      [b cyan]{interaction_cat_name}")
    interaction_list = sort_categories(interaction_list, include_back)
    print_category(interaction_list, 10, True)

    if use_prompt:
        if default is None:
            if go_back is not None:
                prompt = Prompt.ask(f"{third_level_name}", choices=names, default='back', show_choices=False)
                if prompt == 'back':
                    go_back()
            else:
                prompt = Prompt.ask(f"{third_level_name}", choices=names, default=None, show_choices=False)
        else:
            prompt = Prompt.ask(f"{third_level_name}", choices=names, default=default, show_choices=False)
        return prompt


def sort_categories(list: list, include_back: bool = True):
    """Sort categories by priority key.

    Args:
        list (list): list containing all categories to sort.
        include_back (bool, optional): should add back interaction. Defaults to True.

    Returns:
        list: Sorted list.
    """
    found = False
    for index in range(len(list)):
        if list[index]['category_name'] is not None:
            list[index]['priority'] = 1
        else:
            list[index]['priority'] = 0
        if list[index]['category_name'] == 'game':
            if include_back:
                found = True
                add_back = list[index]['data']
                add_back.append({'name': "back", 'desc': 'go back', 'interaction': True})
    if found is False:
        if include_back:
            list.append({'category_name': 'game', 'data':
                        [{'name': 'back', 'desc': "go back", 'interaction': True}],
                        'priority': -1})
    list = sorted(list, key=lambda sort: sort['priority'], reverse=True)
    return list


def print_category(list: list, indentation: int,
                   is_interaction: bool, color: str = 'b white'):
    """Print categories.

    Args:
        list (list): list to process.
        indentation (int): amount of spaces to insert before entries and
        category.
        is_interaction (bool): used for separating interactions and data.
        color (str, optional): color of entries. Defaults to 'b white'.
    """
    for index in range(len(list)):
        category = list[index]['category_name']
        if category is not None:
            print(' ' * (indentation - 2), f"[{color}]{category}:[/{color}]", sep='')

        for n in range(len(list[index]['data'])):
            if list[index]['data'][n] is not None:
                name = list[index]['data'][n]['name']
                if is_interaction:
                    if list[index]['data'][n]['interaction']:
                        names.append(name)
                desc = list[index]['data'][n]['desc']
                if category is not None:
                    if list[index]['data'][n]['interaction'] is True:
                        print(' ' * indentation, f"[magenta]{name}[/magenta] - [gray]{desc}[/gray]", sep='')
                    else:
                        print(' ' * indentation, f"[magenta]{name}[/magenta]: [gray]{desc}[/gray]", sep='')
                else:
                    if list[index]['data'][n]['interaction'] is True:
                        print(' ' * (indentation - 2), f"[magenta]{name}[/magenta] - [gray]{desc}[/gray]", sep='')
                    else:
                        print(' ' * (indentation - 2), f"[magenta]{name}[/magenta]: [gray]{desc}[/gray]", sep='')
        try:
            list.remove(index)
        except ValueError:
            pass  # skip


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
