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

    def put(self, key, item):
        '''If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS: you must
        discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded
        and following by a new line'''
        if key or item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keyse = list(self.cache_data.keys())[0]
            del self.cache_data[keyse]
            print('DISCARD:', keyse)

    def get(self, key):
        '''Must return the value in self.cache_data
        linked to key. If key is None or if the key
        doesn’t exist in self.cache_data, return None.'''
        valor = self.cache_data.get(key)
        if valor:
            return self.cache_data[key]
        return None
