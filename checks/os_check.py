#!/usr/bin/env python3

"""Check for OS and set clear() command.

Returns:
    None
"""

import platform
import os
# os check


def __init__():
    """Detect OS and set the ID."""
    global os_id
    os = platform.system().lower()
    if os == 'linux':
        os_id = 0
    elif os == 'windows':
        os_id = 1
    else:
        os_id = 2


def clear_cmd():
    """Return a clear console command.

    Returns:
        str: Command to clear screen.
    """
    if os_id == 0:
        return 'clear'
    elif os_id == 1:
        return 'cls'
    elif os_id == 2:
        return 'clear'


def clear():
    """Clear screen."""
    os.system(clear_cmd())


__init__()
