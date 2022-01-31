#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""
from typing import Tuple, Union

number = Union[int, float]


def to_kv(k: str, v: number) -> Tuple[str, float]:
    """sum_mixed_list - return basic notation of sum of floats and integers"""
    return (k, v * v)
