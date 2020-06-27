class Solution:
    def thirdMax(self, nums):
        nums=sorted(list(set(nums)))
        # print(nums)
        n=len(nums)
        if n>=3:
            return nums[n-3]
        else:
            return nums[n-1]

A=Solution()
print(A.thirdMax([2,2,3,1]))
