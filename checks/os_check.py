#!/usr/bin/env python3

import platform, os
# os check

os_id = 0

def __init__():
    os = platform.system().lower()
    if os == 'linux': os_id = 0
    elif os == 'windows': os_id = 1
    else: raise NotImplementedError()
    return os_id

def clear_cmd():
    if os_id == 0: return 'clear'
    elif os_id == 1: return 'cls'
    elif os_id == 2: return 'clear'

def clear():
    os.system(clear_cmd())
