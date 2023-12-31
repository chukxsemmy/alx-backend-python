#!/usr/bin/env python3
"""basics of async.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """writes an asyncoronous coroutine
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
