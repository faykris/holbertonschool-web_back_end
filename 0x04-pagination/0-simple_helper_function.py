#!/usr/bin/env python3
"""0. Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index-range: return start and end indexes"""
    s_page = 0
    e_page = page * page_size
    ind = 0

    for pag in range(page):
        for ele in range(page_size):
            ind += 1
        if ind == e_page:
            break
        s_page = ind
    return (s_page, e_page)
