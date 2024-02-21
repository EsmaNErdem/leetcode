# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []

def reverse_linked_list(head):
    prev = None
    node = head
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    return prev