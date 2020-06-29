# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        length = 1
        end = head
        while end.next:
            length += 1
            end = end.next
        k %= length
        if k == 0:
            return head
        mid = head
        for i in range(k-1):
            mid = mid.next
        end.next = head
        new_head = mid.next
        mid.next = None
        return new_head