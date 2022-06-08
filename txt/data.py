#!/usr/bin/env python3

import random as rn

'''
return random data
'''

def random_last():
    with open('txt/last.txt') as last:
        return rn.choice((last.read().splitlines()))

def random_first_male():
    '''
    get male first names from first_name.txt and return random entry; used in new_game()
    '''
    with open('txt/first_male.txt') as male:
        return rn.choice((male.read().splitlines()))

def random_first_female():
    '''
    get female first names from first_female.txt and return random entry; used in new_game()
    '''
    with open('txt/first_female.txt') as female:
        return rn.choice((female.read().splitlines()))

def random_first():
    '''
    merge names from first_male.txt and first_female.txt and return random entry; used in new_game()
    '''
    with open('txt/first_male.txt') as male:
        male = male.read().splitlines()
    with open('txt/first_female.txt') as female:
        female = female.read().splitlines()
    return rn.choice(male + female)

def random_gender():
    '''
    get genders from genders.txt and return random entry; used in new_game()
    '''
    with open('txt/genders.txt') as genders:
        return rn.choice(genders.read().splitlines())

def random_deplete():
    '''
    used in deplete_needs()
    '''
    return rn.randint(0,3)

def random_money():
    '''
    randomize amount of money a player has; used in new_game()
    '''
    return rn.randint(50,500)

def random_fridge():
    '''
    randomize fridge contents when creating a new fridge object
    '''
    return rn.randint(0,10)