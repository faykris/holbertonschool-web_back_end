#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n - make delays as much as n value"""
    wList = []
    for _ in range(n):
        wList.append(await wait_random(max_delay))
    wList.sort()
    return wList
