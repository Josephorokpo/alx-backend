#!/usr/bin/env python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that uses LFU (Least Frequently Used)
    algorithm
    with an LRU (Least Recently Used) tie-breaker.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the class instance.
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

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
                lfu = min(self.frequency.values())
                lfu_keys = []
                for k, v in self.frequency.items():
                    if v == lfu:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for k in lfu_keys:
                        lru_lfu[k] = self.usage.index(k)
                    discard = min(lru_lfu.values())
                    discard = self.usage[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]
            # update usage frequency
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
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
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
