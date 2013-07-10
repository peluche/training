class My_hash:
    """ A naive hashtable (with underlying list) implementation """
    def __init__(self):
        self.__size = 47
        self.__data = [[] for i in range(0, self.__size)]
        self.__setitem__ = self.__a
        self.__getitem__ = self.__g

    def __a(self, key, val):
        """ insert an element """
        index = self.__hash_function(key) % self.__size
        pos = -1
        for ind, i in enumerate(self.__data[index]):
            if i[0] == key:
                pos = ind
                break
        if pos > -1:
            # key already exist
            self.__data[index][pos] = (key, val)
        else:
            # add an entry
            self.__data[index].append((key, val))

    def __g(self, key):
        """ retrieve an element """
        index = self.__hash_function(key) % self.__size
        for i in self.__data[index]:
            if i[0] == key:
                return i[1]
        raise KeyError()

    def __hash_function(self, key):
        res = 0
        for i, j in enumerate(key):
            res += ord(j) * (i + 1);
        return res

def main():
    # test 1 - insert + retrieve
    h = My_hash()
    h['i_am_the_key'] = 'i_am_the_value'
    assert(h['i_am_the_key'] == 'i_am_the_value')

    # test 2 - collision
    h = My_hash()
    h['db'] = 'val 1'
    h['fa'] = 'val 2'
    assert(h['fa'] == 'val 2')
    assert(h['db'] == 'val 1')

    # test 3 - modification
    h = My_hash()
    h['foo'] = 'bar'
    assert(h['foo'] == 'bar')
    h['foo'] = 'baz'
    assert(h['foo'] == 'baz')
    h['foo'] = 'mux'
    assert(h['foo'] == 'mux')

    # test 4 - empty key
    h = My_hash()
    try:
        h['foo']
        assert('should have' == 'raised an exception')
    except KeyError:
        assert('raised :)' == 'raised :)')

if __name__ == '__main__':
    main()
