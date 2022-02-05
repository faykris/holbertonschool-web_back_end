#!/usr/bin/env python3
"""5. LFU Caching"""

from base_caching import BaseCaching
import datetime


class LFUCache(BaseCaching):
    """LFUCache - caching system class """
    action_keys = {}

    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """put - assign dictionary key and their item"""
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.action_keys[key] = datetime.datetime.now()
            elif len(self.cache_data) + 1 > self.MAX_ITEMS:
                most_recent = min(self.action_keys, key=self.action_keys.get)
                self.cache_data.pop(most_recent)
                self.action_keys.pop(most_recent)
                print("DISCARD: {}".format(most_recent))
            self.cache_data[key] = item
            self.action_keys[key] = datetime.datetime.now()

    def get(self, key):
        """get - return value in cache linked to key"""
        if key is not None and key in self.cache_data:
            self.action_keys[key] = datetime.datetime.now()
            return self.cache_data[key]
        else:
            return None
