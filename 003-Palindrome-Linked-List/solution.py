# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        def get_length_linklist(head):
            count = 0
            curr = head
            while curr is not None:
                count+=1
                curr= curr.next
            return count
        length = get_length_linklist(head)
        list1 = []
        list2 = [0]*length
        
        a = length -1
        node = head
        while node is not None:
            list1.append(node.val)
            node =node.next
#       return list1 == list1[::-1]切片
'''         list2[a] = node.val
            a-=1
            node = node.next
        if list1 == list2:#时间复杂度为O(0)
            return True
        else :
            return False
'''
        
