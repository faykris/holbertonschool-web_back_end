#!/usr/bin/env python3
"""6. Complex types - mixed list"""
from typing import List, Union

mxd_typ = List[Union[int, float]]


def sum_mixed_list(mxd_lst: mxd_typ) -> float:
    """sum_mixed_list - return basic notation of sum of floats and integers"""
    return float(sum(mxd_lst))
