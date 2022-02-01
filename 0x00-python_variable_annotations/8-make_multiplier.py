#!/usr/bin/env python3
"""8. Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier - return basic notation of a multiplier function"""
    def mul(n):
        return n * multiplier
    return mul
