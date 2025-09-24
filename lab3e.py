#!/usr/bin/env python3

def give_list():
    return [100, 200, 300, 'six hundred']

def give_first_item():
    my_list = give_list()
    return str(my_list[0])

def give_first_and_last_item():
    my_list = give_list()
    # Corrected to return a list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    my_list = give_list()
    # Corrected to return a list
    return [my_list[1], my_list[2]]
