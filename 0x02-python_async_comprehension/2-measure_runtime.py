#!/usr/bin/env python3
"""module 2"""
import asyncio
from typing import Generator, List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime"""
    ini = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    elapsed = time.perf_counter() - ini
    return elapsed
