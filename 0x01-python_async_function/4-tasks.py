#!/usr/bin/env python3
"""4. Tasks"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n - make delays as much as n value"""
    delays_list = []
    for _ in range(n):
        delays_list.append(await task_wait_random(max_delay))
    return sorted(delays_list)
