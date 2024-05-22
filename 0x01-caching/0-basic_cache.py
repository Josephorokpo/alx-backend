#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that doesn't have any limit.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

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
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data
        , return None.

        Args:
            key: the key to retrieve
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
