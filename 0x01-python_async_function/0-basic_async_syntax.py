#!/usr/bin/env python3
"""0. The basics of async"""
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    time.sleep(delay)
    return delay