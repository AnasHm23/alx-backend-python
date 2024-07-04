#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    returns sum as a float.
    """
    return sum(mxd_list)
