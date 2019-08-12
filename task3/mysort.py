#归并排序
#归并排序，是创建在归并操作上的一种有效的排序算法，该排序算法是采用分治法的一个典型应用
#分治法：
#1）分割：递归地把当前序列平均分割成两半。
#2）集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
def mergeSorted(nums):
    if len(nums)<=1:
        return nums
    middle = len(nums)//2
    # 递归排序左右边,递归地把当前序列平均分割成两半。
    left = mergeSorted(nums[:middle])
    right = mergeSorted(nums[middle:])
    # 用来保存每两边的排序后的结果
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    merged.extend(left if left else right)
    return merged


#快速排序
#快速排序，基准数据找其正确索引位置的过程. 参看https://blog.csdn.net/code_AC/article/details/74158681
# 1、先从数列中取出一个数作为基准数
# 2、分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边
# 3、再对左右区间重复第二步，直到各区间只有一个数

#version1
def qucikSortedV1(nums):
    if len(nums)<=2:
        return nums
    else:
        pivot = nums[0]
        left = [x for x in nums[1:] if x<= pivot]
        right = [x for x in nums[1:] if x> pivot]
        return qucikSortedV1(left)+[pivot]+qucikSortedV1(right)

#不以第一个为基准，而是找到一个合适的基准
def qucikSortedV2(nums,left,right):
    if left < right:
        pivot = Partition(nums,left,right)
        qucikSortedV2(nums,left,pivot-1)
        qucikSortedV2(nums,pivot+1,right)
    return nums

def Partition(nums,left,right):
    pivotkey = nums[left]
    # print(pivotkey)
    while left < right:
        # 从右向左，如果当前指向的元素大于基准的话，向右继续走
        while left < right and nums[right] >= pivotkey:
            right-=1
        nums[left] = nums[right]
        # 从左向右，如果当前指向的元素小于基准的话，向左继续走
        while left < right and nums[left] <= pivotkey:
            left+=1
        nums[right] = nums[left]

    nums[left] = pivotkey
    return left

#插入排序
def insertSorted(nums):
    for i in range(1,len(nums)):
        j = i-1
        key = nums[i]
        # 如果当前的nums[j]大于目前需安排的key的位置，则需要nums[j前面找一个插入的位置，所以将nums[j]往后移动
        # 当key>nums[j]的时候，则为key插入的位置
        while key <nums[j] and j>=0 :
            nums[j+1]=nums[j]
            j-=1
        nums[j+1] = key            
    return nums
            
#冒泡排序
def bubbleSorted(nums):
    
    while True:
        c = 0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                nums[i-1],nums[i] =nums[i], nums[i-1],
                c+=1
        if c == 0:
            break
    return nums


#选择排序
def selectionSorted(nums):
    res = []
    while len(nums)!=0:
        res.append(min(nums))
        nums.remove(min(nums))
    return res





#堆排序

if __name__ == "__main__":
    # print(mergeSorted([7,5,1,6,8,3,13]))
    # print(qucikSortedV1([7,5,1,6,8,3,13]))
    # print(qucikSortedV2([7,5,1,6,8,3,13],0,6))
    # print(insertSorted([7,5,1,6,8,3,13]))
    # print(bubbleSorted([7,5,1,6,8,3,13]))
    print(selectionSorted([7,5,1,6,8,3,13]))