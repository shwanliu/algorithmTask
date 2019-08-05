#三数之和
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        #双指针
        #这边排序可以去重 
        nums=sorted(nums)
        for i in range(0,len(nums)):
            right = len(nums)-1
            left = i+1
            while right > left:
                _sum =nums[i]+nums[right]+nums[left]
                if _sum == 0:
                    res.add((nums[i],nums[right],nums[left]))
                    left += 1
                    right -= 1
                #总和大于0 我们要调整最大的数值，往小的走，
                elif _sum > 0:
                    right -= 1
                #总和小于0 我们要调整小的的数值，往大的走
                else:
                    left += 1
                    
        return list(map(list,res))

#求众数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        #将nums置为set类型，避免了大量的重复计算
        set_ = set(nums)
        for val in set_:
            if nums.count(val) > len(nums)//2:
                return val
        # for key in dic.keys():
        #     if dic[key]>mx_:
        #         return key
