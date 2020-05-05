#!/usr/bin/env python3
"""module 0"""
import asyncio
import random


async def wait_random(max_delay=10):
    """wait_random"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
