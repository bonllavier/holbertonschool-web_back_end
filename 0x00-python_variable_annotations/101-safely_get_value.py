#!/usr/bin/env python3
"""module 101"""
from typing import List, Union, Tuple, Callable, Iterable, Sequence, Mapping, Any, TypeVar
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """"safely get"""
    if key in dct:
        return dct[key]
    else:
        return default
