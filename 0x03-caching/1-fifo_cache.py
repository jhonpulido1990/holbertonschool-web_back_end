#!/usr/bin/python3
""" FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.data = {}
        self.next_in, self.next_out = 0, 0

    def _pop(self):
        """ FIFO algorithm, remove element """
        self.next_out += 1
        key = self.data[self.next_out]
        del self.data[self.next_out], self.cache_data[key]

    def _push(self, key, item):
        """ FIFO algorithm, add element """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.next_out + 1]))
            self._pop()
        self.cache_data[key] = item
        self.next_in += 1
        self.data[self.next_in] = key

    def put(self, key, item):
        """ Assign to the dictionary """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)

    def get(self, key):
        """ Return the value linked """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value


'''Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    You can overload def __init__(self):
    but don’t forget to call the parent init:
    super().__init__()
    def __init__(self): init
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS: you must
        discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded
        and following by a new line
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.current_keys:
                self.current_keys.append(key)
            if len(self.current_keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.current_keys.pop(0)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        Must return the value in self.cache_data
        linked to key. If key is None or if the key
        doesn’t exist in self.cache_data, return None.
        return self.cache_data.get(key)'''
