#用数组实现一个顺序栈
class Stack:
    def __init__(self):
        self.values = []

    def isEmpty(self):
        return self.values == []
    
    def __len__(self):
        return int(len(self.values))
    
    def push(self,value):
        self.values.append(value)

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return;
        return self.values.pop()
#测试
# if __name__ == "__main__":
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     for i in range(len(s)):
#         print(s.values[i])
#     s.pop()
#     for i in range(len(s)):
#         print(s.values[i])

#使用链表实现一个链表栈
class LinkNode:
    def __init__(self, value,next=None):
        self.val = value
        self.next = next

class LinkStack:
    def __init__(self):
        self.head=None
        self.size=0
        self.LinkNode=LinkNode

    def push(self,value):
        # 根据栈的特性，每次插入新的元素，都将这个元素作为head！
        self.head = self.LinkNode(value,self.head)
        self.size+=1
    
    def isEmpty(self):
        return self.head == None

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return;
        p = self.head.next
        self.head = p
    
    def printStack(self):
        p = self.head
        while p!=None:
            print(p.val)
            p = p.next

#测试链表栈
# if __name__ == "__main__":
#     ls = LinkStack()
#     ls.push(1)
#     ls.push(2)
#     ls.push(3)
#     ls.push(4)
#     ls.push(5)
#     ls.push(6)
#     ls.printStack()
#     ls.pop()
#     print("after ls is pop first time")
#     ls.printStack()
#     ls.pop()
#     print("after ls is pop again ")
#     ls.printStack()

#用编程模拟实现一个浏览器的前进、后退功能
#浏览页面的前进和后退，需要用到两个栈，一
# 1.栈X 用来保存开始浏览到当前的界面，即点击前进的时候，压入栈X，
# 2.当用户点击后退是栈X.pop,压入X.pop到栈Y，点击前进的时候就从栈Y取出元素，压入X
class Browser:
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def forward(self,x):
        if len(self.list2)!=0:
            tmp = self.list2.pop()
            self.list1.append(tmp)
        else:
            self.list1.append(x)

    def backward(self):
        x = self.list1.pop()
        self.list2.append(x)
        

    def openNew(self):
        self.list1.clear()
        self.list2.clear()
#测试两个栈实现模拟浏览器的前进和后退
# if __name__ == "__main__":
#     br = Browser()
#     br.forward("百度")
#     br.forward("腾讯")
#     br.forward("阿里")
#     br.forward("字节跳动")
#     #一开始的只有点击进入界面
#     print(br.list1,br.list2)

#     #退一个界面
#     br.backward()
#     print(br.list1,br.list2)
#     #再退一个界面
#     br.backward()
#     print(br.list1,br.list2)
#     #再退一个界面
#     br.backward()
#     print(br.list1,br.list2)
#     #前进
#     br.forward("1")
#     print(br.list1,br.list2)
#     #前进
#     br.forward("2")
#     print(br.list1,br.list2)

#2.用数组实现一个顺序队列,先进先出
class Queue:
    def __init__(self):
        self.values = []

    def isEmpty(self):
        return len(self.values) == 0

    def pop(self):
        if self.isEmpty():
            return;
        return self.values.pop(0)
        
    def push(self,x):
        self.values.append(x)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,index):
        return self.values[index]

# if __name__ == "__main__":
#     q = Queue()
#     q.push(1)
#     q.push(2)
#     q.push(3)
#     q.push(4)

#     for i in range(len(q)):
#         print(q[i])
    
#     q.pop()

#2. 用链表实现一个链式队列
class QueueLink:
    def __init__(self):
        self.head=None
        self.size=0
    
    def push(self,value):
        node = LinkNode(value)
        if self.isEmpty():
            self.head = node
        else:
            tmp = self.head 
            self.head = node
            node.next = tmp
        self.size+=1

    def isEmpty(self):
        return self.head == None
    
    def pop(self):
        if self.isEmpty():
            return
        p = self.head.next
        self.head = p

    def __len__(self):
        return self.size
    
    def __getitem__(self,index):
        p = self.head
        idx = 0
        while idx < index:
            p = p.next
        return p
    
    def printQ(self):
        p = self.head
        while p!=None:
            print(p.val)
            p = p.next

#测试
# if __name__ == "__main__":
#     q = QueueLink()
#     q.push(1)
#     q.push(2)
#     q.push(3)
#     q.printQ()
#     q.pop()
#     q.printQ()
#     q.pop()
#     q.printQ()

#递归：斐波那契数列求值 
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    #非递归
        # a=1
        # b=1
        # while n>2:
        #     c = a+b
        #     a = b
        #     b = c
        #     n-=1
        # return c

# 实现求阶乘 n!
def calc(n):
    if n == 1:
        return 1
    else:
        return n*calc(n-1)

# 实现一组数据集合的全排列
def getSet(nums):
    res = []
    
    def helper(num,r):
        if len(num)==0:
            res.append(r)
        else:
            for i in range(1,len(num)-1):
                r.append(num[i])
                tmp = num
                tmp.remove(num[i])
                helper(tmp,r)

    helper(nums,[])
    return res

if __name__ == "__main__":
    # print(Fibonacci(11))
    # print(calc(4))
    print(getSet([1,2,3]))
