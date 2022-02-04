#!/usr/bin/env python3
"""1. FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache - caching system class """

    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """put - assign dictionary key and their item"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                for key in self.cache_data:
                    print("DISCARD: {}".format(key))
                    self.cache_data.pop(key)
                    break

    def get(self, key):
        """get - return value in cache linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
