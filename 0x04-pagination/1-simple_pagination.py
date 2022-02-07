#!/usr/bin/env python3
"""1. Simple pagination"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page - returns records according page and page_size"""
        if (type(page) == int and page > 0) and\
                (type(page_size) == int and page_size > 0):
            page_tuple = index_range(page, page_size)
            r_list = []
            s_index = page_tuple[0]
            try:
                while s_index < (page_tuple[1]):
                    r_list.append(self.dataset()[s_index])
                    s_index += 1
                return r_list
            except IndexError:
                return []
        else:
            raise AssertionError
