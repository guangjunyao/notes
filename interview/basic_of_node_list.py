class LinkedListError(ValueError):
    pass


class LList:

    def __init__(self):
        self._head = None

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


class ListNode():

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


if __name__ == '__main__':
    mlist1 = LList()
    for i in range(10):
        mlist1.prepend(i)
        mlist1.print_all()


def print_node(head):
    while head is not None:
        print(head.value, '->')
        head = head.next


def length_nodes(head):
    p, count = head, 0
    while p:
        count += 1
        p = p.next
    return count


# # append
# llist0 = ListNode(0)
# head = llist0
# temp = head
# for i in range(1, 10):
#     node = ListNode(i)
#     temp.next = node
#     temp = node
# # print_node(head)

# # prepend
# head = llist0
# for i in range(1, 10):
#     q = ListNode(i)
#     q.next = head
#     head = q
# # print_node(head)

# # insert at k, pre of k is known.
# q = ListNode(11)
# q.next = temp.next
# temp.next = q

# # delete head
# head = head.next

# # delete k
# temp.next = temp.next.next
