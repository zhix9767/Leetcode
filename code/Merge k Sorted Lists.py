# Definition for singly-linked list.
from queue import PriorityQueue

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode()
        cur = head
        query = PriorityQueue()
        for i in lists:
            if i:
                query.put((i.val,i))
        while not query.empty():
            val, node = query.get()
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                query.put((node.val,node))
        return head.next
        