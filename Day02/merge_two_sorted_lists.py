# August-19-2023

# You are given the heads of two sorted linked lists list1 and list2 .
# Merge the two first_lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# Return the head of the merged linked list.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_sorted_linked_lists(
        self, first_list: Optional[ListNode], second_list: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not second_list:
            return first_list
        if not first_list:
            return second_list
        if first_list.val >= second_list.val:
            head_node = second_list
            l1 = second_list
            l2 = first_list
        else:
            head_node = first_list
            l1 = first_list
            l2 = second_list
        while l1 and l2:
            if l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
                l1, l2 = l2, l1
        if not l1:
            temp.next = l2
        return head_node


# YouTube: https://www.youtube.com/watch?v=Xb4slcp1U38&t=1032s
