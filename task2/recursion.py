# -*- coding:utf-8 -*-
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
    def swap(nums_,i,j):
        temp = nums_[i]
        nums_[i] = nums_[j]
        nums_[j] = temp
        
    def perm(nums_,left,right):
        if left==right:
            res.append(nums_)
        else:
            for i in range(left,right+1):
                swap(nums_,i,left)
                perm(nums,left+1,right)
                swap(nums_,i,left)

    perm(nums,0,len(nums)-1)
    return res

if __name__ == "__main__":

    print(getSet([1,2,3]))