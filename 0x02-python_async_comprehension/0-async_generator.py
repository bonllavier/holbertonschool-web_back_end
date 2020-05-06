#!/usr/bin/env python3
"""module 0"""
import random
import asyncio


async def async_generator() -> float:
    """Yield numbers from 0 to `to` every `delay` seconds."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
