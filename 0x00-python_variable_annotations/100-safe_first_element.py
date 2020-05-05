#!/usr/bin/env python3
"""module 100"""
from typing import List, Union, Tuple, Callable, Iterable, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe firts"""
    if lst:
        return lst[0]
    else:
        return None
