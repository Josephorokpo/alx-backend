#!/usr/bin/env python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that uses MRU (Most Recently Used) algorithm.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the class instance.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for
        the key 'key'.
        If key or item is None, this method should not do anything.

        Args:
            key: the key to store the item
            item: the item to store
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.

        Args:
            key: the key to retrieve
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
