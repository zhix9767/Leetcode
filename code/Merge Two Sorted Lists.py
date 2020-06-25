# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        cur = head
        while l1 != None or l2 != None:
            if l1 == None:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            cur = cur.next
        return head.next
        