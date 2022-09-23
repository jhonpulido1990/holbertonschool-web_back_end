#!/usr/bin/env python3
'''Create a class FIFOCache that inherits from
BaseCaching and is a caching system:'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''You can overload def __init__(self):
    but don’t forget to call the parent init:
    super().__init__()'''
    def __init__(self):
        '''init'''
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        '''If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS: you must
        discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded
        and following by a new line'''
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.current_keys:
                self.current_keys.append(key)
            if len(self.current_keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.current_keys.pop(0)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        '''Must return the value in self.cache_data
        linked to key. If key is None or if the key
        doesn’t exist in self.cache_data, return None.'''
        return self.cache_data.get(key)
