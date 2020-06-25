# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        head = ListNode(0,head)
        pre_head = head
        next_head = pre_head.next
        cur = next_head
        while cur:
            next_pre = next_head
            next = cur.next

            temp = next_pre
            count = 1
            while temp.next and count < k:
                temp = temp.next
                count += 1
            if count != k:
                pre_head.next = cur
                return head.next
            
            for i in range(k-1):
                if next:
                    temp = next.next
                    next.next = cur
                    cur = next
                    next = temp
            pre_head.next = cur
            pre_head = next_pre
            next_head = next
            cur = next_head
        
        next_pre.next = None
        return head.next
