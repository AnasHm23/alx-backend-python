#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import Union


def sum_mixed_list(mxd_list: Union[int, float]) -> float:
    """
    Takes a list input_list of floats as argument
    returns their sum as a float.
    """

    return sum(mxd_list)
