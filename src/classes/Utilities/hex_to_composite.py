#!/usr/bin/env python3

# import curses as cs

def hex_to_comp(hex_code: str) -> tuple[int, int, int]:
    MULTIPLIER = 3.9215686274509802
    # omit '#' at beginning

    rgb_red = int(hex_code[1:3], 16)
    rgb_green = int(hex_code[3:5], 16)
    rgb_blue = int(hex_code[5:7], 16)

    # convert to composite and round
    comp_red = round(rgb_red * MULTIPLIER)
    comp_green = round(rgb_green * MULTIPLIER)
    comp_blue = round(rgb_blue * MULTIPLIER)

    return comp_red, comp_green, comp_blue

