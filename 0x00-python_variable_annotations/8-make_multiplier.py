#!/usr/bin/env python3
"""Multiplyer function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A multiplier function
    """
    return lambda x: x * multiplier
