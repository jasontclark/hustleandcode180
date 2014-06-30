#!/usr/bin/env python
""" memcache_homework.py - section 3 homework """
class Memcache(object):

    MEMORY = {}

    def __init__(self):
        global MEMORY
        self.CACHE = MEMORY

    def set(self, key, value):
        self.CACHE[key] = value
        return True

    def get(self, key):
        return self.CACHE.get(key)

    def delete(self, key):
        if key in self.CACHE:
            del self.CACHE[key]

    def flush(self):
        self.CACHE.clear()

def test_memcache():
    m = Memcache()
    print m.set('a', '1')
    print m.set('b', '2')
    print m.CACHE
    print m.get('b')
    print m.get('c')
    m.delete('b')
    print m.CACHE
    m.flush()
    print m.CACHE

if __name__ == '__main__':
    test_memcache()
