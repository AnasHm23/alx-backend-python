#!/usr/bin/env python3
'''declaring a type-annotated function sum_list'''


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as argument
    returns their sum as a float.
    """

    return sum(input_list)
