class My_hash:
    """ A naive hashtable (with underlying list) implementation """
    def __init__(self):
        self.__size = 47
        self.__data = [[] for i in range(0, self.__size)]

    def a(self, key, val):
        """ insert an element """
        index = self.__hash_function(key) % self.__size
        print 'insert [%s] = <%s> index: %d' % (key, val, index)
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

    def g(self, key):
        """ retrieve an element """
        index = self.__hash_function(key) % self.__size
        print 'retrieve [%s] index: %d len: %d' % (key, index, len(self.__data[index]))
        for i in self.__data[index]:
            if i[0] == key:
                return i[1]
        print 'ERROR !'
        return -1

    def __hash_function(self, key):
        res = 0
        for i, j in enumerate(key):
            res += ord(j) * (i + 1);
        return res

def main():
    # test 1 - insert + retrieve
    h = My_hash()
    h.a('i_am_the_key', 'i_am_the_value');
    assert(h.g('i_am_the_key') == 'i_am_the_value')

    # test 2 - collision
    h = My_hash()
    h.a('db', 'val 1')
    h.a('fa', 'val 2')
    assert(h.g('fa') == 'val 2')
    assert(h.g('db') == 'val 1')

    # test 3 - modification
    h = My_hash()
    h.a('foo', 'bar')
    assert(h.g('foo') == 'bar')
    h.a('foo', 'baz')
    assert(h.g('foo') == 'baz')
    h.a('foo', 'mux')
    assert(h.g('foo') == 'mux')


if __name__ == '__main__':
    main()
