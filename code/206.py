# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode=None
        while head:
            postNode=head.next
            head.next=preNode
            preNode=head
            head=postNode
        return preNode