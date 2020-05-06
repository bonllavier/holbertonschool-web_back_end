#!/usr/bin/env python3
"""module 1"""
import random
import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """async_comprehension"""
    result = [i async for i in async_generator()]
    return result
