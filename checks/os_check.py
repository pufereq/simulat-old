#!/usr/bin/env python3

import platform, os
# os check

def __init__():
    global os_id
    os = platform.system().lower()
    if os == 'linux':
        os_id = 0
    elif os == 'windows':
        os_id = 1
    else:
        os_id = 2

def clear_cmd():
    if os_id == 0:
        return 'clear'
    elif os_id == 1:
        return 'cls'
    elif os_id == 2:
        return 'clear'

def clear():
    os.system(clear_cmd())

__init__()