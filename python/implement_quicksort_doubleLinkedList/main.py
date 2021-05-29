class Node:
    def __init__(self, key, next = None, prev = None):
        self._key = key  # key is a dict
        self._next = next
        self._prev = prev

class gamesLinkedList:
    def __init__(self, head = None, tail = None):
        self._head = head
        self._tail = tail
        self._size = 0
    def push_back(self, key):
        node = Node(key, None, None)
        if (self._size == 0):
            self._head = node 
            self._tail = node 
        if (self._size == 1):
            self._tail = node
            node._prev = self._head
            self._head._next = self._tail 
        if (self._size > 1):
            self._tail._next = node
            self._tail._next._prev = self._tail
            self._tail = self._tail._next

        self._size += 1

    def print(self):
        node = self._head
        while(node):
            print(node._key, end= '')
            node = node._next
        print('')


    def partition(self, l, r): 
        size = 1
        node = l
        while node != r:
            node = node._next
            size += 1
        print('size = ', size)

        if size == 1:
            return l
        if size == 2:
            if l._key > r._key:
                self.swap(l, r)
            return l

        k = r._prev


        if k._key > r._key:
            self.swap(r, k)
        
        self.swap(l, k)
        
        pivot = l._key
        i = l
        j = Node(None, None, r)

        

        print('before sort: ', end='')
        self.print()
        i_count = 0
        j_count = size
        print('i = ', i_count)
        print('j = ', j_count)
        while True:
            i = i._next
            i_count += 1
            while i._key < pivot:
                i = i._next
                i_count += 1

            print('i_count = ', i_count)
            j = j._prev
            j_count -=1
            while j._key > pivot:
                j = j._prev
                j_count -=1
            print('j_count = ', j_count)
            print('swap ', i_count, ' and ', j_count)
            self.swap(i, j)
            if (i_count >= j_count):
                break
        if j_count < i_count:
            self.swap(i, j)
        self.swap(j, l)
        print('after sort: ', end='')
        self.print()
        return j

    def preQuickSort(self, l, r):
        if  l != r:
            p = self.partition(l, r)
            if p != l:
                self.preQuickSort(l, p._prev)
            if p != r:
                self.preQuickSort(p._next, r)
    def quick_sort(self):
        self.preQuickSort(self._head, self._tail)

    def swap(self, node1, node2):
        key = node1._key
        node1._key = node2._key
        node2._key = key


if __name__ == '__main__':
    mlist = gamesLinkedList()
    mlist.push_back(3)
    mlist.push_back(6)
    mlist.push_back(2)
    mlist.push_back(1)
    mlist.push_back(8)
    mlist.push_back(4)
    mlist.push_back(5)
    mlist.push_back(7)
    mlist.push_back(0)

    mlist.quick_sort()
    
    mlist.print()
