#!/usr/bin/env python3
"""3. LRU Caching"""

from base_caching import BaseCaching
import datetime


class LRUCache(BaseCaching):
    """LRUCache - caching system class """
    action_keys = {}

    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """put - assign dictionary key and their item"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            self.action_keys[key] = datetime.datetime.now()
            if len(self.cache_data) > self.MAX_ITEMS:
                less_used = min(self.action_keys, key=self.action_keys.get)
                self.cache_data.pop(less_used)
                self.action_keys.pop(less_used)
                print("DISCARD: {}".format(less_used))

    def get(self, key):
        """get - return value in cache linked to key"""
        if key is not None and key in self.cache_data:
            self.action_keys[key] = datetime.datetime.now()
            return self.cache_data[key]
        else:
            return None
