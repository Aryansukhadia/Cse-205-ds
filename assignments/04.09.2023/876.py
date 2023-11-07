# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        temp = head
        prev = None 
        count = 0
        next = None
        while(temp != None):
            count+=1
            temp = temp.next
        # print(count)
        temp = head
        mid = (count)//2
        cnt = 0
        while(cnt <= mid-1):
            cnt+=1
            temp =temp.next

        return temp    
    