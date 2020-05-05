#!/usr/bin/env python3
""""module 8"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiply with callable functionality"""
    def multiply(mult: float) -> float:
        return multiplier * mult
    return multiply
