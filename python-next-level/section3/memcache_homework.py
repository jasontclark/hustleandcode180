

class Memcache(self):
    def __init__(self):
        self.CACHE = {}

    def set(self, key, value):
        pass

    def get(set, key):
        pass

    def delete(self, key):
        pass

    def flush(self):
        pass

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

if __name__ = '__main__':
    test_memcache()
