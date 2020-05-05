#!/usr/bin/env python3
"""module 7"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """"complex operation"""
    return (k, v * v)
