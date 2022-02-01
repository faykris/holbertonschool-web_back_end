#!/usr/bin/env python3
"""0. The basics of async"""
import random
import time
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """wait_random - make delay in range of max_delay"""
    delay = random.uniform(0, max_delay)
    time.sleep(delay)
    return delay
