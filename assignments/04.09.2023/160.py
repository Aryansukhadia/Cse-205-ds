# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        dummyA, dummyB = headA, headB 
        while dummyA != dummyB:
            dummyA = headB if dummyA is None else dummyA.next 
            dummyB = headA if dummyB is None else dummyB.next
      
        return dummyA