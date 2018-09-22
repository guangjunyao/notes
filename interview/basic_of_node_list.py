class ListNode():

    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_


llist1 = ListNode(0)
for i in range(1, 9):
    llist1.next = ListNode(i)


def leng_nodes(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


print(llist1)
