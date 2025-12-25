# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #首先头指针最后变为指向None，所以要定义好pre =None
        pre = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next= pre
            pre = curr
            curr =nxt
            
        return pre
