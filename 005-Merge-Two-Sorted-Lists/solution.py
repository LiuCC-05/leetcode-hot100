# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#迭代的方法
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #补充关于list.sort(key=lambda x: (0, -x.val) if x.val % 2 == 0 else (1, x.val)),就是给每一个对象返回一个key，sort根据key进行排序
        #多条件排序可使用元组Tuple（）
        '''第一种方法：合并两个list，再排序，再连成链表
        list_total=[]
        while list1 is not None :
            list_total.append(list1)
            list1 = list1.next
        while list2 is not None:
            list_total.append(list2)
            list2 = list2.next
        if not list_total:
            return None
        list_total.sort(key = lambda x:(x.val,id(x)))
        for  i in range(len(list_total)-1):
            list_total[i].next =list_total[i+1]
        list_total[-1].next = None#直接选择尾指针
        return list_total[0]
        '''
        #第二种方法
        # 1. 创建一个“虚拟头节点”，它就像是一个临时站台
        # 它的作用是方便我们固定新链表的头部
        dummy = ListNode(0)
        curr = dummy
        
        # 2. 只要两个链表都没走到头，就一直比大小
        # 这是你之前问过的 while 多条件判断！
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1  # 把较小的节点接到新链表后面
                list1 = list1.next # list1 往后移一步
            else:
                curr.next = list2
                list2 = list2.next # list2 往后移一步
            
            curr = curr.next       # 新链表的末尾指针也要往后移一步
            
        # 3. 循环结束后，如果其中一个链表还没走完
        # 我们不需要循环，直接把剩下的那“一串”挂上去即可
        curr.next = list1 if list1 else list2
        
        # 4. 返回虚拟头节点的下一个，即真正的合并后头节点
        return dummy.next

'''递归方法
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 1. 递归出口 (Base Case)：剥到了洋葱的心
        # 如果其中一个链表空了，直接返回另一个链表即可
        if not list1:
            return list2
        if not list2:
            return list1

        # 2. 递归逻辑：谁小，谁就当“头”
        if list1.val <= list2.val:
            # list1 赢了，它作为当前的头节点
            # 剩下的车厢（list1.next 和 list2）该怎么接？
            # 重新交给这个函数去处理，处理完后挂在 list1.next 上
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # list2 赢了，它作为当前的头节点
            # 剩下的车厢（list1 和 list2.next）交给递归处理
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
'''
