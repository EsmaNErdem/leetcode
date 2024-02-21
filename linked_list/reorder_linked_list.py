# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

def reorder_linked_list(head):
    if not head: return []

# bring slow to middle of the linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next

# reverse the right half of the linked
    node, prev = slow.next, None
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

# close left end with tail
        slow.next = None

# merge left half with the reverse right half
    current_left, current_right = head, prev

    while current_right:
        next_left = current_left.next
        next_right = current_right.next
        # append nodes
        current_left.next = current_right
        current_right.next = next_left

        current_left = next_left
        current_right = next_right

    return current_left

    