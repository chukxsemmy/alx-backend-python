#!/usr/bin/env python3
"""takes a list of integers and returns sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns integer sum as float"""
    return sum(mxd_lst)
