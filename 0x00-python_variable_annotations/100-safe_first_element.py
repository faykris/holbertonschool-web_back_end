#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""
from typing import Iterable, List, Sequence, Tuple, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns a first element of a sequence, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
