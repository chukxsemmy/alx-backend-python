#!/usr/bin/env python3
"""Appropriate type  values
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns function with appropriate types
    """
    return [(i, len(i)) for i in lst]
