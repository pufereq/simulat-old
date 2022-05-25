#!/usr/bin/env python3

# get random names from text files
import random as rn

def random_last():
    with open('txt/last_uni.txt') as last:
        return rn.choice((last.read().splitlines()))

def random_first_male():
    with open('txt/first_male.txt') as male:
        return rn.choice((last.read().splitlines()))

def random_first_female():
    with open('txt/first_female.txt') as female:
        return rn.choice((last.read().splitlines()))

def random_first():
    with open('txt/first_male.txt') as male:
        male = male.read().splitlines()
    with open('txt/first_female.txt') as female:
        female = female.read().splitlines()

    return rn.choice(male + female)

def random_gender():
    with open('txt/genders.txt') as genders:
        return rn.choice(genders.read().splitlines())

def random_number():
    return rn.randint(0,3)