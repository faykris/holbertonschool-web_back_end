#!/usr/bin/env python3
"""4. Tasks"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n - make delays as much as n value"""
    wList = []
    for i in range(n):
        wList.append(await task_wait_random(max_delay))
    return wList
