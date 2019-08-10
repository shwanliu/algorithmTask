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

#version1.直接取每一个递归list中的第一个元素作为基准元素
def qucikSortedV1(nums):
    if len(nums)<=2:
        return nums
    else:
        pivot = nums[0]
        left = [x for x in nums[1:] if x<= pivot]
        right = [x for x in nums[1:] if x> pivot]
        return qucikSortedV1(left)+[pivot]+qucikSortedV1(right)

# def qucikSortedV2
# #插入排序

#冒泡排序


#选择排序


#堆排序

if __name__ == "__main__":
    print(mergeSorted([7,5,1,6,8,3,13]))
    print(qs([7,5,1,6,8,3,13]))