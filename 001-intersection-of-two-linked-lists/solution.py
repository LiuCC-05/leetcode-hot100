# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#第一种方法：长度差法
'''class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def get_linklist_length(head):
    count = 0
    current = head 
    while current is not None:
        count+=1
        current =current.next

    return count


class Solution(object):

    def getIntersectionNode(self,headA,headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        IntersectionNode=None
        lengthA=get_linklist_length(headA)
        lengthB=get_linklist_length(headB)
        diff = abs(lengthA-lengthB)
        
        if lengthA>lengthB:
            for _ in range(diff):
                headA = headA.next
            while headA is not headB:
                headA=headA.next 
                headB=headB.next
            return headA
        
        else:
            for _ in range(diff):
                headB = headB.next
            while headB is not headA:
                headA=headA.next 
                headB=headB.next
            return headA
'''
#第二种方式：双指针法
class Solution(object):
    def getIntersectionNode(self,headA,headB):
        if headA is None or headB is None:
            return None
        
        pA = headA
        pB = headB
        while pA is not pB:
            if pA is None :
                pA =headB
            else:
                pA = pA.next
            if pB is None:
                pB=headA
            else:
                pB = pB.next
        return pA  #返回的都是当下的pA值所以当pA和pB 没有交点都走完了双方所有的长度之后，pA和pB此时都是为None，循环也就停止了，所以也就不存在循环一直发生的情况

            


