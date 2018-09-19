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
        while(count < k and current is not None):
            current = current.next
            count += 1
        # if current is None, k is greater or equal to the number of nodes, don't change the list
        if current is None:
            return 
        k_th_node = current # store current to k th node
        while current.next is not None:
            current = current.next # point to the last node
        current.next = head # change next of last node to previous head   
        head = k_th_node.next # change head to k+1 node
        k_th_node.next = None # change next of k th node to NULL
        
