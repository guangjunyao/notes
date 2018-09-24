class LinkedListError(ValueError):
    pass


class LList:

    def __init__(self):
        self._head = None

    def __iter__(self,):
        p = self._head
        while True:
            try:
                yield p.value
            except:
                break
            p = p.next

    def __len__(self,):
        p, count = self._head, 0
        while p:
            count += 1
            p = p.next
        return count

    def is_empty(self):
        return self._head is None

    def pop(self,):
        if self._head is None:
            raise LinkedListError('pop error')
        e = self._head.value
        self._head = self._head.next
        return e

    def prepend(self, elem):
        self._head = ListNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = ListNode(elem)
            return
        p = self._head
        while p is not None:
            p = p.next
        p.next = ListNode(elem)

    def pop_last(self,):
        if self._head is None:
            raise LinkedListError('pop last error')
        p = self._head
        if p.next is None:  # only one element
            e = p.value
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.value
        p.next = None
        return e

    def delete(self, k):
        count = k
        if self._head is None:
            raise LinkedListError('empty list')

        if k == 0:  # special case, prepend
            self._head = self._head.next
            return
        p = self._head
        while p is not None and count > 1:  # find the prev of k
            count -= 1
            p = p.next
        try:
            p.next = p.next.next
        except AttributeError:
            raise LinkedListError('out of bounds')

    def insert(self, k, elem):
        count = k
        if self._head is None:
            self._head = ListNode(elem, self._head)
            return
        if k == 0:  # special case, prepend
            self._head = ListNode(elem, self._head)
            return
        p = self._head
        while p is not None and count > 1:  # find the prev of k
            count -= 1
            p = p.next
        q = ListNode(elem)
        try:
            q.next = p.next
            p.next = q
        except AttributeError:
            raise LinkedListError('out of bounds')

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.value):
                return p.value
            p = p.next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.value):
                yield p.value
            p = p.next

    def print_all(self,):
        p = self._head
        while p is not None:
            print(p.value, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print()

    def elements(self,):
        p = self._head
        while p is not None:
            yield p.value
            p = p.next

    def apply(self, proc):
        p = self._head
        while p is not None:
            proc(p.value)
            p = p.next

    def reverse(self,):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next  # get the first node
            q.next = p  # reverse one by one
            p = q
        self._head = p

    def sort1(self,):
        if self._head is None:
            return
        cur = self._head.next
        while cur is not None:
            x = cur.value
            p = self._head
            while p is not None and p.value <= x:
                p = p.next
            while p is not cur:
                y = p.value
                p.value = x
                x = y
                p = p.next
            cur.value = x
            cur = cur.next


class ListNode():

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


mlist1 = LList()
a = [1, 4, 3, 2, 5, 2]
for i in a:
    print(i)
    mlist1.append(i)
mlist1.print_all()
