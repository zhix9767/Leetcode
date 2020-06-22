# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        result = head
        carry=0
        while(l1!=None or l2!=None):
            val1 = l1.val if l1!=None else 0
            val2 = l2.val if l2!=None else 0
            result.next = ListNode((val1+val2+carry)%10)
            carry = (val1+val2+carry)/10
            l1 = l1.next if l1!=None else l1
            l2 = l2.next if l2!=None else l2
            result = result.next
        if carry==1:
            result.next=ListNode(carry)
        return head.next
