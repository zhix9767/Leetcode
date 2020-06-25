# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        remove_pre = head
        current = head
        for i in range(n-1):
            current = current.next
        if current.next == None:
            return head.next
        current = current.next
        while current.next != None:
            current = current.next
            remove_pre = remove_pre.next
        remove_pre.next = (remove_pre.next).next
        return head

        