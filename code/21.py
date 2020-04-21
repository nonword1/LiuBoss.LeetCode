# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        res = ListNode(-1)
        if l1.val<l2.val:
            res.val = l1.val
            res.next = self.mergeTwoLists(l1.next,l2)
        else:
            res.val = l2.val
            res.next = self.mergeTwoLists(l1,l2.next)
        return res