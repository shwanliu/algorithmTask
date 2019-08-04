# Task 1: 数组和链表（2天）
### 时间：2019-08-03 21:00 - 2019-08-05 21:00 
### 讨论&CR时间: 2019-08-05 21:00 - 2019-08-05 22:30

### [数组]
    1. 实现一个支持动态扩容的数组
    2. 实现一个大小固定的有序数组，支持动态增删改操作
    3. 实现两个有序数组合并为一个有序数组
    4. 学习哈希表思想，并完成leetcode上的两数之和(1)及Happy Number(202)！(要求全部用哈希思想实现！)（选做）（注意：在第四天会进行继续学习）

### [链表]
    1. 实现单链表、循环链表、双向链表，支持增删操作
    2. 实现单链表反转
    3. 实现两个有序的链表合并为一个有序链表
    4. 实现求链表的中间结点

### 对应LeetCode练习题
    Three Sum（求三数之和）
        英文版：https://leetcode.com/problems/3sum/
        中文版：https://leetcode-cn.com/problems/3sum/

    Majority Element（求众数）
        英文版：https://leetcode.com/problems/majority-element/
        中文版：https://leetcode-cn.com/problems/majority-element/

    Missing Positive（求缺失的第一个正数）[作为可选]
        英文版：https://leetcode.com/problems/first-missing-positive/
        中文版：https://leetcode-cn.com/problems/first-missing-positive/

    Linked List Cycle I（环形链表）
        英文版：https://leetcode.com/problems/linked-list-cycle/
        中文版：https://leetcode-cn.com/problems/linked-list-cycle/
        
    Merge k Sorted Lists（合并 k 个排序链表）
        英文版：https://leetcode.com/problems/merge-k-sorted-lists/
        中文版：https://leetcode-cn.com/problems/merge-k-sorted-lists/

CSDN: c++ https://blog.csdn.net/tyxacm/article/details/88321206

# 思路

### 1. 实现一个支持动态扩容的数组

    a) 类的构造函数，赋予该类的初始化：
        #参数（容量capacity，当前数组长度size，数组元素data）
    
    b) 插入元素函数：
        #参数（需要给定插入位置index，相应的元素x）
        必须以下几步：
        （1）对index进行有效性的判断；
        （2）判断是否需要进行扩容；
        （3）在指定的位置插入数据，需要将index+1后面的数据向后移动一位，然后再将x添加到index；
    （4）更新参数size +=1

    c) 扩容函数，将原本的array扩充两倍，或者更多：
        #参数（新的动态数组的容量）
        （1）新建一个更大的动态数组
        （2）将原本的data赋值到新的动态数组里面
        （3）需要更新变量，capacity以及data

### 2. 实现一个大小固定的有序数组，支持动态增删改操作
        
    a) 类的构造函数，赋予该类的初始化：
        #参数（容量capacity，当前数组长度size，数组元素data）
    
    b) 插入元素函数，需要插入排序算法，才能得到一个有序的数组：
        #参数：等待插入的元素x
        必须有以下几步：
        （1）判断当前的size是否需要进行扩容；
        （2）在确定好新元素插入位置，需要将插入位置后的元素往后面移动
        （3）更新参数size +=1。

    c) 扩容函数，将原本的array扩充两倍，或者更多：
        #参数（新的动态数组的容量）
        （1）新建一个更大的动态数组
        （2）将原本的data赋值到新的动态数组里面
        （3）需要更新变量，capacity以及data

    d) 删除元素函数，根据index删除对应元素：
        #参数（index）
        （1）判断index的合法性，是否在[0,size-1]的范围之类
        （2）删除index的元素后，将[index+1, size-1]的元素向前移动
        （3）更新参数size -=1

    e）修改元素函数，修改对应位置的元素
        #参数（需要给定修改位置index，改后的元素x）
        （1）直接删除给定index的元素
        （2）插入x元素，得到一个排序好的数组

### 3. 实现一个大小固定的有序数组，支持动态增删改操作
    使用有序数组的方式，直接让最后的数组等于其中一个，遍历一遍另外一个数组进行插入

### 4. 
    a)两数之和，使用字典存储下标以及对应的val，只要遍历一遍nums，得到每一次遍历的target-val是否在dic中，在直接break掉后返回

    b)happy number: 使用dic存储下1-9的平方，如果出现循环的情况即，得到的sum和在之前出现过（或者是1出现了，之后一直会出现也是要break的），所以维护一个set，如果在set则说明出现了无限循环，break掉后，返回n==1



