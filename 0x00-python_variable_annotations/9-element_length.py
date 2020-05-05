#!/usr/bin/env python3
"""module 9"""
from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck tape"""
    return [(i, len(i)) for i in lst]
