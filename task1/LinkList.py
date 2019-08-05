# -*- coding:utf-8 -*-
# 定义链表节点
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
# 单链表类的定义，支持增删
class LinkList:
    def __init__(self,):
        # 指定一个头
        self.head = None
    # 给定一个列表包含了nums，进行初始化
    def initlist(self,nums):
        self.head = Node(nums[0])
        p = self.head

        for val in nums[1:]:
            node = Node(val)
            p.next = node
            p = p.next
    #获取当前的链表长度，方便其他操作的参数进行有效合法性判断的使用
    def getlength(self):
        p = self.head
        length = 0
        while p!= None:
            length+=1
            p = p.next
        return length
    # 检查当前的链表是否为空
    def isEmpty(self):
        return self.getlength() == 0

    #清空列表
    def clear(self):
        self.head = None

    #增加链表元素
    def append(self,value):
        q = Node(value)
        if self.head == None:
            self.head = q
        else:
            p = self.head
            while p.next!=None:
                p = p.next
            p.next = q    
    #返回对应index下标的元素
    def getitem(self,index):
        if self.isEmpty():
            print("error LinkList is empyt.")
            return
        j = 0
        p = self.head

        while p.next!=None and j<index:
            p = p.next
            j+=1
        
        if j== index:
            return p.val
        else:
            print("target is not exist!")
    #通过下标和元素，插入元素
    def insert(self,index,value):

        if self.isEmpty() or index < 0 or index > self.getlength():
            print("LinkList is empty or index is illegal.")
            return;
        
        if index == 0:
            q = Node(value, self.head)
            self.head = q

        p =self.head
        tmp = self.head
        j = 0 
        while p.next!=None and j<index:
            tmp = p
            p = p.next
            j+=1
        if index ==j:
            q = Node(value)
            tmp.next = q
            q.next = p

    #根据下标删除元素
    def delete(self,index):
        if self.isEmpty() or index < 0 or index > self.getlength():
            print("LinkList is empty or index is illegal.")
            return;
        if index == 0:
            q = self.head.next
    
        p = self.head
        tmp = self.head
        j = 0
        while p.next!=None and j<index:
            tmp = p
            p = p.next
            j +=1 
        
        if index == j:
            tmp.next = p.next
    #根据元素值来查找index
    def search_by_value(self,value):

        if self.isEmpty():
            print("error LinkList is empyt.")
            return;
        
        p = self.head
        i = 0
        while p.next!=None and not p.val==value:
            p = p.next
            i+=1
        
        if p.val == value:
            return i
        else:
            return -1

#测试   
# if __name__ == "__main__":
#     l = LinkList()
#     l.initlist([x for x in range(100)])
#     print (l.getitem(7))
#     l.append(6)
#     print (l.getitem(5))

#     l.insert(4,999)
#     print (l.getitem(13))
#     print (l.getitem(24))
#     print (l.getitem(15))

#     l.delete(5)
#     # l.clear()
#     print (l.getitem(5))
#     l.search_by_value(5)

#==============================================================================
# 这边实现一个单向循环链表，最后一个节点不指向None，而是指向第一个元素
class CycleSingleLinkList:
    def __init__(self):
        self.head = None
    # 检查当前链表是否为空
    def isEmpty(self):
        return self.head is None
    # 获取当前链表的长度
    def getlength(self):
        if self.isEmpty():
            return 0
        length = 1
        p = self.head
        #当遇到当前节点指向的下一个节点是头节点的时候就是遍历完了一遍链表
        while p.next != self.head:
            length+=1
            p = p.next
        return length
    #添加元素,头部添加
    def add(self,value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
            node.next = self.head
        else:
            # 将添加的节点的下一位指向头节点
            node.next = self.head
            # 接下来遍历一遍到之前的尾节点进行指向新添加的节点
            p = self.head
            while p.next != self.head:
                p = p.next
            p.next = node
            self.head = node
    #添加元素，尾部添加
    def append(self,value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
            node.next = self.head
        else:
            p = self.head
            while p.next!=self.head:
                p = p.next
            p.next = node
            node.next = self.head
    
    def insert(self,index,value):
        if self.isEmpty() or index < 0 or index > self.getlength():
            print("LinkList is empty or index is illegal.")
            return;
        node = Node(value)
        p = self.head
        idx = 0
        while idx < (index-1):
            idx+=1
            p = p.next
        node.next = p.next
        p.next = node


    def delete(self,index):
        if self.isEmpty() or index < 0 or index > self.getlength():
            print("LinkList is empty or index is illegal.")
            return;
        p = self.head
        if index == 0:
            if p.next!=self.head:
                while p.next!=self.head:
                    p = p.next
                p.next = self.head.next
                self.head = self.head.next
            else:
                self.head = None
        else:
            idx = 0
            pre = self.head
            while p.next != self.head and idx<index:
                pre = p
                p = p.next
                idx +=1
            if index==idx:
                pre.next = p.next 

#测试   
# if __name__ == "__main__":
#     ll= CycleSingleLinkList()

#     ll.add(1)
#     # p = ll.head
#     # while p.next!=ll.head:
#     #     print(p.val)
#     #     p = p.next
#     # print ("length1:",ll.getlength())

#     ll.add(2)
#     ll.append(3)
#     ll.insert(2, 4)
#     ll.insert(4, 5)
#     ll.insert(0, 6)
#     p2 = ll.head
#     while p2.next!=ll.head:
#         print(p2.val)
#         p2 = p2.next
#     print ("length:",ll.getlength())
#     ll.delete(1)
#     print ("length:",ll.getlength())

#==============================================================================
# 双向链表，只完成插入,
# 需要重新定义链表节点
class DNode:
    def __init__(self,prev_,next_,value):
        self.prev = prev_
        self.next = next_
        self.value = value

class DoubleLink:
    def __init__(self):
        self.head = DNode(None,None,None)
        self.head.prev = self.head
        self.head.next = self.head
        self.nCount = 0
    
    def getlenghth(self):
        return self.nCount
    
    def isEmpty(self):
        return self.nCount==0

    # 后插
    def insert(self,index,value):
        p = self.getitem(index)
        node = DNode(None,None,value)
        node.prev = p
        node.next = p.next
        p.next.prev = node
        p.next = node
        self.nCount+=1

    def getitem(self,index):
        if index<0 or index>self.nCount:
            print("out of range")
            return;
        if index==0:
            return self.head
        # 使用二分正向查找
        if index < self.nCount / 2:
            p = self.head.next
            i = 0
            while i <index -1 :
                p = p.prev
                i+=1
            return p
        p = self.head.prev
        rindex = self.nCount - index
        j = 0
        while j < rindex:
            p = p.prev
            j+=1
        return p

    # 获取index位置节点的值
    def getNodeValue(self, index):
        return self.getitem(index).value
# 测试
# if __name__ == '__main__':
#     dlt = DoubleLink()
#     # 头节点下标为0
#     dlt.insert(0, 12)
#     dlt.insert(1, 13)
#     dlt.insert(1, 14)
#     print('---------------------------')
#     for i in range(dlt.nCount+1):
#         print(i, ':', dlt.getNodeValue(i))
#     print('size:', dlt.nCount)


#2. 实现单链表反转，效率特别低，之后在做修改。。。，leetcode上已经AC
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        r = ListNode(0)
        if head == None:
            return
        def helper(head,r):
            p = head
            prev = p
            if p.next==None:
                r.next = p
                return r.next
            while p.next:
                prev = p
                p = p.next
            r.next = p
            r = r.next
            prev.next = None
            helper(head,r)
                
        helper(head,r)
        return r.next

# 合并两个有序链表
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        r = res
        if l1 is None:
            return l1
        elif l2 is None:
            return l2
        # 在l1和l2同时不为空的情况下进行比较
        while l1 and l2:
            if l1.val < l2.val:
                r.next = l1
                l1 = l1.next
            else:
                r.next = l2
                l2 = l2.next   
        r = r.next
        if l1 is not None:
            r.next = l1 
        else:
            r.next = l2
        return res.next

# 实现求链表的中间节点，有点作弊嫌疑
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p = head
        if head ==None:
            return None
        l = []
        while p!=None:
            l.append(p)
            p = p.next
        # print(l[len(l)//2])
        return l[len(l)//2]