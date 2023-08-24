# August-24-2023

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer. Internally, pos is used to denote the
# index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
from typing import Optional, Any


class ListNode:
    def __init__(self, val: Any):
        self.val = val
        self.next = None


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        ptr1 = ptr2 = head
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr2 == ptr1:
                return True
        return False
