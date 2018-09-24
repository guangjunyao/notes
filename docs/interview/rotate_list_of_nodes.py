from copy import copy


class ListOfNodes:

    def __init__(self, x):
        self.value = x
        self.next = None


class Rotation:

    def rotate_to_end(self, head, k):
        if k == 0:
            return head

        current = copy(head)
        count = 1
        while (count < k and current is not None):
            current = current.next
            count += 1
        # if current is None, k is greater or equal to the number of nodes, don't change the list
        if current is None:
            return
        k_th_node = current  # store current to k th node
        while current.next is not None:
            current = current.next  # point to the last node
        current.next = head  # change next of last node to previous head
        head = k_th_node.next  # change head to k+1 node
        k_th_node.next = None  # change next of k th node to NULL


def print_node(head):
    while head is not None:
        print(head.value, '->')
        head = head.next


llist0 = ListOfNodes(0)
head = llist0
# 向后插入, 初始化
for i in range(1, 10):
    node = ListOfNodes(i)
    head.next = node
    head = node

# length of node list
head = llist0
next_ = current.next
current.next = prev
prev = current
current = next_
# count = 1
# for i in range(2):
#     head = head.next
# # reverse a node list
# temp = []
# while head is not None:
#     temp.append(head.value)
#     print(head.value, '->')
#     head = head.next
# llist1 = ListOfNodes(temp[-1])
# head = llist0

# for i in reversed(temp):
#     node = ListOfNodes(i)
#     head.next = node
#     head = node
print_node(head)


# rotate to the end
def swap_list(head, from_, to_):
    count = 1
    for i in range(from_):
        head = head.next

    # while count <= to_ and head is not None:
    # head =
