#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-task').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n - make delays as much as n value"""
    wList = []
    for _ in range(n):
        wList.append(await task_wait_random(max_delay))

    return sorted(wList)
