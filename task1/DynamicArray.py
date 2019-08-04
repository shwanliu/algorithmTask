# -*- coding:utf-8 -*-

#1.实现一个支持动态扩容的数组
class DynamicArray_1:
    # 初始动态数组的构造函数
    # 需要内定义内部参数：capacity 指定初始数组的容量，
    # data元素
    def __init__(self,capacity = 10):
        # 数组最大容量
        self.capacity = capacity  
        # 非空的数值 size
        self.size = 0
        # 初始化默认capacity大小的元素
        self.data = [None]*self.capacity

    # 插入元素，
    def add(self,index,x):
        # 1.indexde的合法判断
        if (index<0 or index>self.size):
            print("Your input index: %d is error,check one more time!"%index)
            return;

        #2.判断容量capacity是否能够承受新的元素添加
        #a.已经到达capacity的话，扩容
        if (self.size == self.capacity):
            self.resize(self.capacity*2)
        #b.不到达的话，根据index添加元素之后，index之后的元素往后移动一位
        for i in range(self.size-1, index-1,-1):
            self.data[i+1] = self.data[i]
        self.data[index] = x
        #4.更新当前动态数组的self.size
        self.size += 1

    # 扩容数组函数
    def resize(self, capacity):
        #1. 新建一个更大容量的数组
        newarr = DynamicArray_1(capacity)
        #2. 将现在self.data的元素逐个拷贝到新数组
        for i in range(self.size):
            newarr.add(i, self.data[i])
        #3. 更新变量
        self.capacity = capacity
        self.data = newarr.data
# 测试
# if __name__ == "__main__":
#     arr = DynamicArray_1(10)
#     for i in range(32):
#         # print(i)
#         arr.add(i,i+1)

#     for j in range(arr.size):
#         print(arr.data[j])

#==============================================================================
#2.实现一个大小固定的有序数组，支持动态增删改操作
class DynamicArray_2:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.data = [None]*self.capacity
    
    #插入函数，得到的是有序的数组
    def add(self,x):
        if self.size==0:
            self.data[0] = x
            self.size +=1
            return
        # 如果当前的数组长度大于这个数组的最大容量的话，我们需要进行扩容 
        if (self.size==self.capacity):
            self.resize(self.capacity*2)
        # 倒序遍历数组，移动后面的元素，等待一个位置插入
        for i in range(self.size,-1,-1):
            if x < self.data[i-1]:
                self.data[i] = self.data[i-1]
            else:
                break
        #此时的i就是我们要插入的位置了
        self.data[i] = x
        self.size+=1

    # 扩容函数
    def resize(self, capacity):
        newarr = DynamicArray_2(capacity)
        for i in range(self.size):
            newarr.data[i] = self.data[i]
        self.capacity = capacity
        self.data = newarr.data

    #删除函数
    def delet(self,index):
        if index<0 or index>self.size-1:
            print("Your input index: %d is error,check one more time!"%index)
            return;
        
        #删除了对应index的元素，需要向前移动元素
        for i in range(index+1,self.size,1):
            self.data[i-1] = self.data[i]
        
        #更新你的size
        self.size -= 1

    #修改函数
    def update(self,index,x):
        if index<0 or index>self.size-1:
            print("Your input index%d is error,check one more time!"%index)
            return;
        
        self.delet(index)
        self.add(x)

# 测试
# if __name__ == "__main__":
#     arr = DynamicArray_2(10)
#     for i in range(20,0,-1):
#         arr.add(i)
#     # arr.delet(5)
#     # arr.delet(18)
#     arr.update(6,999)
#     for j in range(arr.size):
#         print(arr.data[j])

#==============================================================================
#3.实现两个有序数组合并为一个有序数组

def beOneArray(array1,array2):

    if array1.size==0:
        return array2
    elif array2.size==0:
        return array1
    
    resArray = array1
    for j in range(array2.size):
        resArray.add(array2.data[j])
    return resArray

# 测试
# if __name__ == "__main__":
#     arr1 = DynamicArray_2(10)
#     for i in range(80,20,-2):
#         arr1.add(i)

#     arr2 = DynamicArray_2(10)
#     for i in range(20,10,-1):
#         arr2.add(i)
     
#     print("start")
#     resarr = beOneArray(arr1,arr2)
#     for j in range(resarr .size):
#         print(resarr.data[j])

# 4 学习哈希表思想，并完成leetcode上的两数之和（1）以及happy Number（202）！（）要求全部用哈希思想实现！）（选做）
# python中使用字典来做为hashmap
# 两数之和
def twoSum(nums,target):
    # 定义一个字典
    dic={}
    #遍历一边nums
    for i,m in enumerate(nums):
        # 如果target - m 的值在dic中的话，直接返回了
        if dic.get(target - m) is not None:
            return [i,dic.get(target - m)]
        #不然一直添加key和value到dic字典
        dic[m]=i
        #没有的话直接返回空list
        return []

#happy Number
def isHappy(n):

    set_ = set()
    dic = {}
    # 来保存1-9的平方
    for i in range(10):
        dic[str(i)] = i**2
    sum_ = 0
    #不出现循环的，出现了则跳出来
    while n not in set_:
        sum_=0
        for val in str(n):
            sum_ += dic[val]
        set_.add(n)
        n = sum_
    # 判断n是否为1，为1则True，不为1为False
    return n == 1

if __name__ == "__main__":
    # print(twoSum([2,7,11,15],9))
    print(isHappy(19))

