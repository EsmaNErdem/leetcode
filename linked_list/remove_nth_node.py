# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Input: head = [1], n = 1
# Output: []

# Input: head = [1,2], n = 1
# Output: [1]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_node(head, n):
    def length(head):
        count = 0 
        node = head
        while node:
            count += 1
            node = node.next

        return count
    
    lenght_of_ll = length(head)
    index = lenght_of_ll - n + 1
    node = head
    curr = None

# this will stop right before the desired node
    for _ in range(1, index):
        curr = node
        node = node.next

# that means it is the first node so return next node or None
    if curr == None:
        return head.next
    
    else:
        curr.next = node.next.next
        return head
