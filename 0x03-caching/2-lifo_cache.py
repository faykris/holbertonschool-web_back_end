#!/usr/bin/env python3
"""2. LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache - caching system class """
    last_key = None

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
                self.cache_data.pop(self.last_key)
                print("DISCARD: {}".format(self.last_key))
            self.last_key = key

    def get(self, key):
        """get - return value in cache linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
