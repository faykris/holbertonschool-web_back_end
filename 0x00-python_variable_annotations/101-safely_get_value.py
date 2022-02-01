#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""
from typing import Iterable, List, Sequence, Tuple, Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """returns a dict or a default value (type variable or None)"""
    if key in dct:
        return dct[key]
    else:
        return default
