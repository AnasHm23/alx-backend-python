#!/usr/bin/env python3
'''declaring a type-annotated function sum_list
'''


def sum_list(input_list: list[float]) -> float:
    '''Returns the sum of the list as float'''
    return sum(input_list)
