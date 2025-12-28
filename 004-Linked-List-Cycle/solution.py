# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:#这里面可以排除掉fast =None,1.头节点为None，只有一个节点，到达最后一个节点.next = None
            slow = slow.next
            fast = fast.next.next
            if fast == slow :
                return True
        return False
