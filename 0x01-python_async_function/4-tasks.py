#!/usr/bin/env python3
"""module 4"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n"""
    list1 = []
    for x in range(n):
        list1.append(await task_wait_random(max_delay))
    return sorted(list1)
