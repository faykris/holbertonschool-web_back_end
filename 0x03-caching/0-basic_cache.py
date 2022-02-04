#!/usr/bin/env python3
"""0. Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache - caching system class """

    def put(self, key, item):
        """put - assign dictionary key and their item"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """get - return value in cache linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
